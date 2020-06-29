# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:38:06 2020

@author: SATHWIK
"""


def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s


# given string
mystr = "BeginnersBook"
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))