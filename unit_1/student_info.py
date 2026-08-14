# Collect user information
name = input('Enter your name: ')
surname = input('Enter your last name: ')
age = int(input('Enter your age: '))
favourite_number = float(input("Enter your favourite number: "))

# Concatenate name and surname to get the full name of the user and store it in variable full_name
full_name = name +' '+ surname
print(f'{name.upper()}')
print(f'{name.title()}')

#  Calculate the age that the user provides, conver the age to months, multiplying it by 12 (representing months)
age_in_months = age * 12

# Convert the age in months to string
age_in_months = str(age_in_months)

# Next few lines of code display the information.

print(f'Your age is {str(age)} in months is: {age_in_months}')
print(f'Your favourite number is {round(favourite_number,2)}')
print(f'Welcome,{full_name.title()} ')