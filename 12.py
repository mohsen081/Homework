# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:30:09 2019

@author: OFOK
"""

def uniqe_list (x):
    x = list(set(x))
  
    return x

a = [1,2,3,3,3,3,4,5]
print a
print uniqe_list(a)