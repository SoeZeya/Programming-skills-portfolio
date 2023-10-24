# -*- coding: utf-8 -*-
"""
Chapter3.Exercise6

You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    
"""

# Initial list of guests
Guests = ["Jeff", "Nick", "Ralph", "Kelvin", "Peter"]

# Print a message stating that only two people can be invited for dinner
print("Sorry, Dinner is limited due to some problems. Only two people can be invited for dinner.")

while len(Guests) > 2: #using while loop to filter the guests
    removedGuest = Guests.pop() # Using pop method to remove guests
    print("Sorry,", removedGuest, "The dinner is canceled")


for guest in Guests: # Printing message for the two remaining guests
    print(guest, "you're still invited to dinner.")


del Guests[:] # Using del method to remove the last two names from the list
print("Guests list is now empty:", Guests)

