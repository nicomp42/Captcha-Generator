#main.py
# Name:Josh Halbakken
# email:halbakjc@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date:2-29-24
# Course/Section:ADV APP DEV (001)
# Semester/Year:spring 2024
# Brief Description of the assignment:make improvements to a random captcha generatr
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. 
#allows users to generate random captchas
# Citations:
# Anything else that's relevant: 
'''
Created on Feb 26, 2020

@author: nicomp
'''

from Src.Assignment07 import generate_captcha

result = generate_captcha()
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

