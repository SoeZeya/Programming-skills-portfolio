# -*- coding: utf-8 -*-
"""
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

places_to_visit = ["Germany", "French", "Italy", "Denmark", "Greenland"] # List of places to visit

print("Original order:", places_to_visit) # Print the original list

print("Alphabetical order:", sorted(places_to_visit)) # Use sorted() to print the list in alphabetical order without modifying it

print("Original order (unchanged):", places_to_visit) # Printing original list to show it's still in its original order
 
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True)) # Using sorted() to print the list in reverse alphabetical order

print("Original order (unchanged):", places_to_visit)  # Printing original list to show it's still in its original order

places_to_visit.reverse() # Using reverse() to change the order of the list
print("Reversed order:", places_to_visit)

places_to_visit.reverse() # Using reverse() again to revert to the original order
print("Back to original order:", places_to_visit)

places_to_visit.sort() # Using sort() to change the list to alphabetical order
print("Sorted in alphabetical order:", places_to_visit)

places_to_visit.sort(reverse=True) # Using sort() to change the list to reverse alphabetical order
print("Sorted in reverse alphabetical order:", places_to_visit)
