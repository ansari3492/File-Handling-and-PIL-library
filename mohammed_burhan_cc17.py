# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:50:08 2018

@author: Lenovo
"""

from PIL import Image
img_filename=Image.open("day4/sample.jpg")

img_filename = img_filename.convert('LA')
img_filename = img_filename.rotate(-90)

width, height = img_filename.size 
x = width/2
y= height/2

img_filename = img_filename.crop((x-80, y-102, x+80, y+102))


img_filename.thumbnail((75,75))
img_filename.show()
img_filename.save("cropped.png")
