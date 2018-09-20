#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re

# Assignment Week 2

# Example text
# x= "Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ..."
#
# y = re.findall('[0-9]',x)
# print y

# First, open regex_sum_42.txt file, and read all the text in a variable sausage
f = open("regex_sum_42.txt","r")
sausage = f.read()
x = re.findall('[0-9]+',sausage)
# sum all the strings found
# 1. str to int
# 2. sum
print x
