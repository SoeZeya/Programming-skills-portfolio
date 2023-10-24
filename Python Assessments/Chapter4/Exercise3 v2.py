# -*- coding: utf-8 -*-
"""
Chapter4.Exercise3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

#Version2
alien_color = 'Yellow' #Declaring variable for alien color
x=input("What's the color of the Alien (Red,Green,Yellow only): ") #asking user input


# Checking the condition
if x == alien_color:
    print("Congratulations! You just earned 5 points for shooting the green alien.") #printing state 1
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.") #printing state 2
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.") #printing state 3