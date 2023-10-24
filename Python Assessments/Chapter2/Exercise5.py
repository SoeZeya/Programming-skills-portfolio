# -*- coding: utf-8 -*-
"""
Chapter2Exercise5
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""
cost = 6 #declaring variable for cost of the USB stick

budget = 50 #decaring variable for budget she have
Pamount = budget // cost #decaring variable to calculate the amount of USB stick she can buy
budget = budget % cost #Declaring variable to calculate the money left from the budget

print("USB amount she can buy: ", Pamount) #printing USB amount she can buy
print("badget left",budget ) #printing badget left
