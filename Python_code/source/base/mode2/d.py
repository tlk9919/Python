#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 9:44
# @Author  : 刘宇
# @File    : d.py
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
@property
def my_age(self):
    print(self__age,end='')
@my_age.setter
def my_age(self,age):
                self.__age=age
if __name__ == "__main__":
    p=Person("张三",20)
    print(p.my_agw,'a',sep=',')
    p.my_age=25
    print(p.my_age,'b',sep=',')
    run_code = 0
