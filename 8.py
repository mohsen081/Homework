# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:55:05 2019

@author: OFOK
"""
def printlist():
    a = [5, 10, 15, 20, 25]
    return [ a[i] for i in (0, -1) ]
print printlist()