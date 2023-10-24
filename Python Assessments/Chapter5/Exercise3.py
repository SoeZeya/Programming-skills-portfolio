# -*- coding: utf-8 -*-
"""
Chapter5 Exercise3

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.
"""

# Creating glossary (dictionary)
programming_glossary = {
    'variable': 'A container for storing data in a program.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a specified condition is met.',
    'list': 'A data structure that stores a collection of items in a specific order.',
    'integer': 'A data type representing whole numbers.',
    'string': 'A data type representing text or characters.',
    'boolean': 'A data type representing true or false values.',
    'dictionary': 'A data structure that stores key-value pairs.',
    'module': 'A file containing Python code that can be imported and used in other programs.',
    'Array': 'An array is a data structure used in computer programming to store a collection of elements, all of which must be of the same data type',
    'Control structure': ' control structure is a block of code that determines the flow of program execution.',
    
}

#Printing each word and its meaning using a loop
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")#using f to create a formatted string. using \n as mentioned in the questionS
