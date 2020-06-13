#! usr/bin/env python
# coding=utf-8
# Author="张维序"

"""
1、注册账户
2、登录账户
3、获取昵称
"""


def register(file):
    """
    实现账号注册功能
    :return:
    """
    username = input("请输入账号：\n")
    password = input("请输入账号密码：\n")
    temp = username + "|" + password
    with open(file, 'w+') as fp:
        fp.write(temp)


register(".\login.md")


def login():
    """
    实现登录账号
    :return:
    """
    username = input("请输入账号：\n")
    password = input("请输入账号密码：\n")
    with open(".\login.md", "r") as fp:
        info = fp.read()
        info = info.split("|")  # 字符串切割成列表
        print(info)
        if username == info[0] and password == info[1]:
            print("登录成功")
        else:
            print("登录失败")


login()
