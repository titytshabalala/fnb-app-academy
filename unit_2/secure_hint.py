"""
Challenge: The Secure Password Hint Tool

Create a script that helps users showing them a secure hint.

1. Ask the user to input their secret password.
2. User .strip() to clean up any accidental spaces they might have typed at the start or end.
3. Grab the very first letter and the very last letter of the password using string indexing.
4. Print a hint using an f-string that forces the letters into uppercase so they stand out. (e.g,Your password hint: It starts with P and ends with N)
"""


# Collect the user's secret password.
user_name = input("Please enter your secret password: ").strip()

print(f"Your password hint: It starts with {user_name[0].upper()} and ends with {user_name[-1].upper()}")