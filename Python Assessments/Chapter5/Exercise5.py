# -*- coding: utf-8 -*-
"""
Chapter5 Exercise5
Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets.
Next, loop through your list and asyou do, print everything you know about each pet
"""

# Creating dictionaries for pet and owners
pets = [
    {'animal': 'Dog', 'owner': 'Jeff'},
    {'animal': 'Cat', 'owner': 'Kevin'},
    {'animal': 'Sugar Glider', 'owner': 'Alice'},
    {'animal': 'Rabbit', 'owner': 'Mayce'},
]

#Using for loop to loop through the list
for pet in pets:
    kind = pet['animal']
    owner = pet['owner']
    print(f"The {kind} is owned by {owner}.")
