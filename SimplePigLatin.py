__author__ = 'trevorbillwaite'

# Week Three Assignment
# Introduction to Computer Science
# SimplePigLatin.py

# Program will prompt the user to enter an English word to translate; then it will translate the word in to Simple Pig Latin; and lastly it will print the translated word.

# Prompt the user.

word = input("Please enter any word in the English lanquage: ")



# Translate the word.

# Define vowels.
vowels = "aeiouAEIOU"

if word[0] in vowels:
    # Print translated word that started with a vowel.
    print((word + "yay").capitalize())
    
else:
    # Print translated word that start with a consonant.
    print((word[1:] + word[0] + "ay").capitalize())
    
    # To fix the capitalization issue, add .capitalize() to the end of what was being printed.  By doing so, the code is instructing that he word that is printed will have the first letter upper case and the rest of the letters lower case.
    