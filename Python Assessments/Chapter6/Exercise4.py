# -*- coding: utf-8 -*-
"""
Chapter6 Exercise4
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
# Creating a list of sandwich orders
sandwich_orders = ['tuna', 'turkey','chicken', 'veggie','ham']

# Creating an empty list for finished sandwiches
finished_sandwiches = []

while sandwich_orders:

    order_to_make = input("what would you like to make (type 'quit' to finish): ")#choosing what order to make from the sandwish order

    if order_to_make == 'quit':
        break  # Exit the loop if 'quit' is entered

    if order_to_make in sandwich_orders: 
        print("I made your",order_to_make," Sandwish.")
        finished_sandwiches.append(order_to_make)#using append method to add into the finished order
        sandwich_orders.remove(order_to_make)#using remove method to remove from sandwish order
    break #using break, so that the next printing state will work
# Prinring sandwish that were made
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(finished_sandwiches)
    break
