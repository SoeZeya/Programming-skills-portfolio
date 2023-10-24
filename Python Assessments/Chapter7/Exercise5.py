# -*- coding: utf-8 -*-
"""
Chapter7 Exercise5

Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence,such as Reykjavik is in Iceland.
Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(city, country="UAE"):#creating function
    print(city,"is in",country)

describe_city("Dubai")#Using the default country
describe_city("Yangon", "Myanmar")
describe_city("Tokyo", "Japan")
