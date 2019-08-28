# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:11:20 2019

@author: OFOK
"""

def max(a,b,c):
    mx=a
    if b>mx and b>c:
        mx=b
    else:
        if c>mx and c>b:
            mx=c
    return mx

print max(10,8,20)