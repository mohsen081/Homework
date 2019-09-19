# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:55:18 2019

@author: OFOK
"""

def ch_prim (n):
    x=range(n)
    x.remove(0)
    x.remove(1)
    p=[1 for i in x if n%i==0]
    if sum(p) <= 0:
        print ("The number is prime")
    else:
        print("The number is not prime")
number=int(input("pleas enter your number: "))
ch_prim (number)
