# -*- coding: utf-8 -*-
"""
Chapter4.Exercise2
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""
#Version1, in this version user will enter Green and it will run if block
x=alien_color = 'green' #Declaring variable for alien color

input("What's the color of the Alien: ")#asking user input for the alien colors
# Checking the condition
if x== alien_color:
    print("Congratulations! You just earned 5 points for shooting the green alien.") #printing state1
else:
    print("Congratulations! You just earned 10 points for shooting the alien.")#printing state2
