#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql


if __name__ == '__main__':
    db = pymysql.connect(host="10.211.55.13", port=3306, user="chengcheng", password="mysql@Centos01",
                         database="d_erp_order")
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 使用 fetchone() 方法获取单条数据.

    cursor.execute("use d_erp_order")

    # 关闭数据库连接
    db.close()

