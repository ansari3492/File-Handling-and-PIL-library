# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:14:37 2018

@author: Lenovo
"""
n=50
for number in range(1,n+1):
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif not number%5:
        print( "Buzz")
    elif not number%3:
        print( "Fizz")
    else:
        print(number)
    
    
    

    

