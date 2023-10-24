# -*- coding: utf-8 -*-
"""
Chapter6 Exercise1
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
As they enter each topping,print a message saying you’ll add that topping to their pizza.
  
"""

#Declaring list for pizza
Ptoppings = []

while True: #using True to repeatly ask user to add topping
    topping = input("Enter a pizza topping (type 'quit' to finish): ") #asking user input for topping 
    
    if topping == 'quit': #if user type 'quit',the loop will break
        break   #if user type 'quit',the loop will break
    else:
        print(f"Adding {topping} to your pizza.")
        Ptoppings.append(topping) #using append method to add topping to the list when user add something

# Printing state
if Ptoppings: #if user add something for the topping, the message will appear like this
    print("\nYour pizza will have the following toppings:")
    for topping in Ptoppings:
        print(topping)
else: #if user choose 'quit' in above question, the message will appear like this
    print("You didn't choose any toppings for your pizza.")

