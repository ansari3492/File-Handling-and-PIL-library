# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:58:43 2018

@author: Lenovo
"""
  
        
    
def translate(str):
    consonants='bcdfghjklmnpqrstvwxyz'
    print("".join(l+'o'+l if l in consonants else l for l in str))

    
string=input("Enter Any String: ")

translate(string)