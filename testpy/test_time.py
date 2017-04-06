#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import timeit
  
n = 10000

def test_range(n):
	for i in range(n):
		pass
	return i

#print('Python', python_version())
  
print('ntiming range()')
timeit.timeit(test_range(n))
#print(test_range(n))

