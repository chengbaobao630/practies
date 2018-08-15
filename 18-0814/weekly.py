#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import time
from datetime import timedelta, datetime
from enum import Enum
import pythoncom
import mammoth
import win32com.client as win32
from docx import Document
from bs4 import BeautifulSoup


class DateType(Enum):
    this_week = 0
    next_week = 1
    after = 2


now = datetime.now()
this_week_start = now - timedelta(days=now.weekday())
this_week_end = now + timedelta(days=6 - now.weekday())


def get_job(type, num) -> str: return "get_job"


def get_content(type, num) -> str: return "get_content"


def get_finish(_, num) -> str: return "get_content"


def get_unfinished(_, num) -> str: return "get_unfinished"


def get_time(_, num) -> str: return "get_time"


def get_result(_, num) -> str: return "get_result"


def get_unfinished_trace() -> str: return "get_unfinished_trace"


def get_qa() -> str: return "get_qa"


def get_next_week_expect_result() -> str: return "get_next_week_expect_result"


def get_support() -> str: return "get_support"


this_week = {
    "submit_time": this_week_end.strftime("%y/%m/%d"),
    "start_time_end_time": "{0}至{1}".format(this_week_start.strftime("%y/%m/%d"),
                                            this_week_end.strftime("%y/%m/%d")),
    "job_": get_job,
    "content_": get_content,
    "finish_": get_finish,
    "unfinished_": get_unfinished,
    "unfinished_trace": get_unfinished_trace,
    "Q&A": get_qa,
    "support": get_support,
    "result_": get_result,
}

next_week = {
    "job_": get_job,
    "job_content_": get_content,
    "job_time_": get_time,
    "expect_result": get_next_week_expect_result
}

after = {
    "job_": get_job,
    "job_content_": get_content,
    "job_time_": get_finish
}


def do(cell_param, type_in, week_params, prefix):
    for key, value in week_params.items():
        if prefix:
            key = prefix + key
        if key.endswith("_"):
            key += "."
        m_in = re.compile(".*{0}.*".format("{" + key + "}"))
        if re.search(m_in, cell_param.text):
            if type(value) == str:
                cell_param.text = cell_param.text.replace("{" + key + "}", value)
            else:
                # cell_param.text = value()
                rs = re.search("\d", cell_param.text)
                if rs and rs.group():
                    if "support" == key:
                        print(key)
                        print(rs.group())
                    cell_param.text = value(type_in, rs.group())
                else:
                    cell_param.text = value()


def do_this_week(cell_param):
    do(cell_param, DateType.this_week, this_week, "")


def do_next_week(cell_param):
    do(cell_param, DateType.next_week, next_week, "next_week_")


def do_after(cell_param):
    do(cell_param, DateType.after, after, "after_")


def handler(cell_param):
    do_this_week(cell_param)
    do_next_week(cell_param)
    do_after(cell_param)


def sendemail(sub, body, file_path):
    outlook = win32.Dispatch('outlook.application')
    namespace = outlook.GetNamespace('MAPI')
    receivers = ["799096114@qq.com", '554858452@qq.com']
    mail = outlook.CreateItem(0x0)
    mail.To = receivers[0]
    mail.CC = '1060471903@qq.com;554858452@qq.com'
    # mail.BCC = ['1060471903@qq.com', "799096114@qq.com"]
    mail.Subject = sub
    # mail.Body = MIMEText(body)
    mail.HTMLBody = body
    # 添加附件
    mail.Attachments.Add(file_path)
    mail.Send()


if __name__ == '__main__':
    subject = "{0}_工作周报_{1}~{2}".format("程呈", this_week_start.strftime("%y-%m-%d"),
                              this_week_end.strftime("%y-%m-%d"))
    file_name = "{0}.doc".format(subject)
    document = Document("weekly-template.docx")
    r = re.search("\d", "{support}")
    if r and r.group():
        print(r.group())
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                handler(cell)
    document.save(file_name)
    # time.sleep(2)
    with open(file_name, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value  # The generated HTML
        messages = result.messages  # Any messages, such as warnings during conversion
        soup = BeautifulSoup(html, 'html.parser')
        table_html = soup.table
        table_html["border"] = "1px solid"
        table_html["style"] = "border-collapse: collapse"
        for tr in soup.find_all("tr"):
            tds = tr.contents
            td_length = len(tds)
            if td_length < 5:
                if td_length >= 2:
                    tds[1]["colspan"] = 6-td_length
                elif td_length == 1:
                    tds[0]["colspan"] = 5
                else:
                    continue
        sendemail(subject, """<html>
	        <head>
	            </head>
	            <body>{0}
                </body>
            </html>""".format(soup.prettify()), os.path.dirname(os.path.realpath(file_name)) + os.path.altsep + file_name)
