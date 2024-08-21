#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
#print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
#print(validUTF8(data))

#data = [229, 65, 127, 256]
#data = [197, 130, 1]
#data = [145]
data = [240, 162, 138, 147, 145]
#expected val = False
print(validUTF8(data))
