# -*- coding: utf-8 -*-
"""
Chapter5 Exercise4
Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

# Creating dictionary of rivers
rivers = {
    'Ayeyarwaddy': 'Myanmar',
    'Amazon': 'Brazil',
    'Mississippi': 'United States'
}

#Using loop to print a sentence
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")#using f to create a formatted string.
    
#Using loop to print name of rivers
print("\nRivers:")
for river in rivers.keys():
    print(river)
    
#Using loop to print name of Countries
print("\nCountries:")
for country in rivers.values():
    print(country)
