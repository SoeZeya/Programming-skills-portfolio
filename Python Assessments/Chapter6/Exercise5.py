# -*- coding: utf-8 -*-
"""
Chapter6 Exercise5
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

#Creating list for sandwish order
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'ham', 'pastrami']

# Creating empty list for finished sandwiches
finished_sandwiches = []

# Printing message that run out of pastrami
print("Sorry,we're out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')#using remove method to remove pastrami from the list

while sandwich_orders:
    print("Available sandwich orders:") #printing available sandwish order without pastrami
    for order in sandwich_orders:
        print(order)

    order_to_make = input("What would u like to make (or 'quit' to finish): ")

    if order_to_make== 'quit':
        break  # Exit the loop if 'quit' is entered

    if order_to_make in sandwich_orders:
        print("I made your",order_to_make,"sandwich.")
        finished_sandwiches.append(order_to_make)
        sandwich_orders.remove(order_to_make)
        break

# Printing finished sandwish
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(finished_sandwiches)
