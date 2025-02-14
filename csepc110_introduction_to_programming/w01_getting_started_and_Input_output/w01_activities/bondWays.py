"""
Author: Moïse Marc-Aurel MASSAMBA-DILUEKI,

Purpose: This program asks the user for their name and repeats it back in the way of James Bond, "Bond, James Bond"
"""
#ask for user name
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
#display user name in the way of James Bond
print(f"Your name is {lastName.title()}, {firstName.title()} {lastName.title()}")