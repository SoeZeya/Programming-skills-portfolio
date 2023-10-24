# -*- coding: utf-8 -*-
"""
A movie theater charges different ticket prices depending on a person’s age.
If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
"""

while True: #using True in while loop to ask user continuesly until they choose something
    age = int(input("Please enter your age (Type 'quit' to exit): "))

    if age == 'quit':
        break  #if user type 'quit',the loop will break.
        
        #this is the printing state by ages respectively
    if age < 3:
        print("Your ticket is free.")
        break
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
        break
    else:
        print("Your ticket costs $15.")
        break
 #using break after every printing state to stop the loop after the option.
