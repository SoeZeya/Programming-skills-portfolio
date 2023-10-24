# -*- coding: utf-8 -*-
"""
Chapter3.Exercise 5

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""

Guests = ["Jeff", "Nick", "Ralph", "Kelvin", "Peter"] #declearing the guest list 

# Replace the guest who can't make it with a new person
unavailableGuest = "Kelvin" #declaring variable guesst who can't make it
newGuest = "Stella" #declaring variable for the new guest

if unavailableGuest in Guests:
    
    Guests.remove(unavailableGuest) #Remove the unavailable guest
    Guests.append(newGuest) #adding new guest using append method

# Print invitation messages for the remaining guests
for guest in Guests:
    print("Dear " ,guest, "You are cordially invited to our event on Saturday. Please join us for a great time!")
