#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

"""
1、==：内容与类型必须同时满足
2、assert in ：后者包含前者  Python自动化测试实战  测试实战
3、is ：前后两个值相等

"""




import pytest
def add(a, b):
	return a + b


def test_add_001():
	assert add(1, 1) == 2


def test_add_002():
	assert add(1, 1) != "2"

def test_in():
	assert  "测试实战" in "Python自动化测试实战"


str1="admin"
str2="admin"
str3="admind"

def test_is():
	assert  str1 is str2



if __name__ == '__main__':
	pytest.main(["-v"])

