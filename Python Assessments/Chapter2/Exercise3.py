# -*- coding: utf-8 -*-
"""
#Chapter2 Exercise3
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""
name= "\t\n Soe Zeya \n\t" #declaring the person name using white space character

print("lstrip():", name.lstrip()) #print using lstrip function
print("rstrip():", name.rstrip()) #print using rstrip function
print("strip():", name.strip()) #print using strip function