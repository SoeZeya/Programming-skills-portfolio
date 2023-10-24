# -*- coding: utf-8 -*-
"""
Chapter4.Exercise1
Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green.
If it is, print a message that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails.
(The version that fails will have no output.)
"""
#Version2
alien_color = 'green' #first declaring variable for alien color
input("Enter the color of the Alien: ") #asking user input for the alien color

if alien_color == 'green': # Checking user input tht the color is right with the system color
    print("Congratulations! You just earned 5 points.") #Printing congratulation cuz the user input is match with system color
#this is for the fail state, user might input wrong color, I did't write any other code for print. cuz there will be no output for fail state