"""
Multi-Function Calculator

Building calculator program that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.


Requirements:
> use float(input()) to collect two numbers from the user
> Calculate and display: addition, subtraction, multiplicatoin, division
> Calculate and display: floor division (//) and modulus (%)
> Round all results to 2 decimal places using round()
> Handle division by zero, if the second number is 0, display friendly error message instead of crashing
> Display all results in a formatted table using f-strings

"""

# First number to enter

num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))
operator = input("Would you like to (+),(-), (\u00F7), or (x): ")

if operator == "+":
    result = num_1 + num_2
    print(f"{round(result,2)}")
elif operator == "-":
    result = num_2 - num_1
    print(f"{round(result,2)}")
elif operator == "x":
    result = num_1 * num_2
    print(f"{round(result,2)}")
elif operator == "/" or operator == "\u00F7":
    if num_2 == 0:
        print(f"Cannot divide by 0")
    else:

        result = num_1 / num_2
        print(f"{round(result,2)}")

floor_div = num_2 // num_1

modulus_result = num_2 % num_1


print(f"Floor divisoin:\t{round(floor_div,2)}\nModulus:\t{round(modulus_result,2)}")