__author__ = 'trevorbillwaite'

# Week Three Assignment
# Introduction to Computer Science
# StarWarsName.py

# Program will prompt the user to input their first and last name, their mother's maiden name, and the city where they where born.  It will also calculate and print out their "Star Wars" name.


# Prompt the user...

last = input("Please enter your last name: ")
first = input("Please enter your first name: ")
maiden = input("Please enter your mother's maiden name: ")
city = input("Please input the name of the city in which you were born: ")


# Calculate the "Star Wars" name.

    # Calculate "Star Wars" first name.
StarWarsFirst = last[0:3] + first[0:2]

    # Calculate "Star Wars" last name.
StarWarsLast = maiden[0:2] + city[0:3]


# Print out the "Start Wars" name.

print(StarWarsFirst.capitalize() , StarWarsLast.capitalize())