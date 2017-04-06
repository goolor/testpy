#!/usr/bin/env python3
#-*- coding: utf-8 -*-

str1=r"'test string' new line"
print("Original is:"+str1)
print()
print("After repr is:"+repr(str1))
print()
#print("After eval is:"+eval(str1))
print()
#print("After repr(eval is:"+repr(eval(str1)))
print()
print("After eval(repr is:"+eval(repr(str1)))

