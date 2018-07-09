#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import pymysql

name = "cc"
print("%s hello" % (name.capitalize()))
print("%s hello" % (name.center(40, "*")))

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
'''
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")
'''
age = [1, 2, 3]
it = iter(age)
for a in age:
    print(a)
print(a)


def test():
    b = a + 10
    print(b)


test()


matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]
print(sys.path)
'''
db = pymysql.connect(host="172.19.26.64", port=3306, user="root", password="mysql@Centos01", charset='utf8',
                     database='d_chaogou')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()


sql = '''
    # select * from t_ts_wx_black_eye_info
'''

cursor.execute(sql)

black_eyes = cursor.fetchall()

for black_eye in black_eyes:
    print(black_eye)


print("Database version : %s " % data)

# 关闭数据库连接
db.close()

#  datasource:
#    url: jdbc:mysql://192.168.1.102:3306/d_md_two_shop?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true
#    username: root
#    password: mysql@Centos01
#    driver-class-name: com.mysql.jdbc.Driver
#  jpa:
#    hibernate:
#      ddl-auto: create

'''


def test_default(username="cc"):
    print(username)

test_default("haha")
test_default()

print(r'^admin/')
