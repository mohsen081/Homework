# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:29:16 2019

@author: OFOK
"""
number = int (input ("Please choose a number to divide:"))

l = list (range (1, number ))
x=0
for num in l:
    if number% num == 0:
        x=x+1
if x>1:
    print ("not prime")
else:
    print ("prime")
        