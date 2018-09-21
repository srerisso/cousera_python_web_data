#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re

# Assignment Week 2

# First, open regex_sum_42.txt file, and read all the text in a variable sausage
# f = open("regex_sum_42.txt","r")
f = open("regex_sum_139199.txt","r")
sausage = f.read()
chunk = re.findall('[0-9]+',sausage)
# sum all the strings found
# 1. str to int
# 2. sum
sum = 0
for x in chunk:
    sum = int(x) + sum

print sum
