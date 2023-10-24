# -*- coding: utf-8 -*-
"""
Chapter5 Exercise2

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters.
Use these words as the keys in your glossary, and store their meanings as values.

Print each word and its meaning as neatly formatted output.
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output. 
"""

#Creating glossy dictionary
glossary = {
    'variable': 'A container for storing data in a program.',
    'function': 'A reusable block of code that performs a specific task.',
    'Array': 'An array is a data structure used in computer programming to store a collection of elements, all of which must be of the same data type',
    'Control structure': ' control structure is a block of code that determines the flow of program execution.',
    'list': 'A data structure that stores a collection of items in a specific order.'
}

#printing the word followed by colon and its meaning 
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n") #using f to create a formatted string. using \n as mentioned in the questionS
