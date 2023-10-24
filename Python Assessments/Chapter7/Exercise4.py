# -*- coding: utf-8 -*-
"""
Chapter7 Exercise4

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="large", message="I love Python"):
    
    print(size,"-sized shirt with the message:",message)

make_shirt() #Creating large shirt with the default message

make_shirt(size="medium") #Creating medium shirt with the default message

make_shirt(size="small", message="Python is fun!")#Creating medium shirt with the default message
