# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:15:17 2019

@author: OFOK
"""

def fact (n):
    if n<= 0:
        return 1
    else:
        return (n*fact(n-1))
number=int(input("pleas enter your number: "))
if number >0:
    print fact(number)
else:
    print("The number is negative")