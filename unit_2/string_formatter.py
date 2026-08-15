""""
Write a Python script that takes a user's first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text

Requirements:
1. Collect user information (first name, last name & bio)
2. Create a user name by combining the first initial + last name in lowercase (e.g jdoe)
3. Display the full name in title case (Jane Doe)
4. Strip leading/trailing whitespace from the bio before displaying it
5. Count and display the number of characters in the bio using len()
6. Replace any occurence of 'I am' in te bio with "I'm" using .replace()
7. Display all output using f-strings
"""

# Collect user first and last name var: first_name; last_name

first_name = input("Enter your first name: ").strip().title()
last_name = input("Enter your last name: ").strip().title()
# Create a username

username = first_name[0].lower() + last_name.lower()

# Collect the user's bio var: bio

bio = input("Enter your bio:\n").strip().replace("I am","I'm")

# Display user's full name var: full_name

full_name = first_name + last_name

# Count and Display number of characters var: char_length_bio


char_length_bio = len(bio)

print(f"Full Name:\t{full_name}\nUsername:\t{username}\nBio\n{bio}\t{char_length_bio}")