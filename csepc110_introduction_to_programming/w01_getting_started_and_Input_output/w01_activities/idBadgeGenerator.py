"""
Author : Moïse Marc-Aurel MASSAMBA-DILUEKI, Brother Burton

Purpose : Building ID Badge Generator and Practice formatting strings.
"""

print("Please enter the following information: ")

# This prints a blank line
print()

#ask for user basic information
firstName = input("What is your first name ? ").title()
lastName = input("What is your last name ? ").upper()
email = input("What is your e-mail address ? ").lower()
phone = input("What is your phone number ? ")
job = input("What is your Job Title ? ").title()
id = input("What is your Id Number ? ")

# Ask for the additional information
hairColor = input("What is your color's hair? ").capitalize()
eyesColor = input("What is your color's eyes? ").capitalize()
month = input("Type your started month : ").capitalize()
training = input("Did you complete advanced training? Answer Yes or No :").capitalize()

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("-"*50)
print(lastName +', '+ firstName)
print(job)
print(f"ID: {id}")
print()
print(email)
print(phone)
print(f"Hair: {hairColor:15} Eyes: {eyesColor}")
print(f"Month: {month:14} Training: {training}")
print("-"*50)