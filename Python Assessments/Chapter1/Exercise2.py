# -*- coding: utf-8 -*-
"""
Chapter1 Exercise2
Write a Python program to get the Python version you are using.

"""

import sys #import sys library from the python build-in library function

version = sys.version #decalring variable for the python version, and call the version from sys library
print("Python version: ",version)

info= sys.version_info #declaring variable for the version info and call the version_info from the sys library
print("Version info:", info)