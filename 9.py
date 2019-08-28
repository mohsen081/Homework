# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:05:36 2019

@author: OFOK
"""

def new_list (x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

a = [1,2,3,4,3,2,1]
print a
print new_list(a)