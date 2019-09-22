# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:26:40 2019

@author: OFOK
"""
def ch_perf (n):
    l = list (range (1, n))
    sum=0
    for num in l:
        if n% num == 0:
            sum=sum+num
    return sum
number=int(input("pleas enter your number: "))
sum=ch_perf(number)
if (sum == number):
   print ("The number is a perfect")
else:
   print("The number is not a perfect")


