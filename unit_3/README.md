# Unit 3
## Arithmetic Operations and Type Casting

- Unit 3 introduces core mathematical operationas that form the basis of         calculations in Python programs.

- performining arithmetic using Python's seven operators: _+, -, /, //, %, **_
- Explain the difference between integer division (__//__) and regular division (__/__)
- Converting between data types using int(), float(), and str()

- Apply round() and abs() to numeric values.
- Build a multi-function calculator using arithmetic and type casting

## Manipulating Numbers
### Arithmetic Operators
- Python supports seven arithmetic operators. Addition (+), Subtraction (-), Multiplicatoin (*), and Division (/) work as expected. Division always returns a float, even for whole numbers: *10/2* gives *5.0* not 5. Floor (*//*) discards the decimal: *10//3* gives 3. Modulus (%) returns only the remainder: *10%3* gives 1. Exponentiation (**) raises to a power: 2**10 gives 1024.


## The Type Casting Gotcha
__input()__ always returns a string. This causes a very common beginner error: if you write _num = input('Enter a number:')_ and then try num + 5, Python will raise a __TypeError__ because you cannot add a string and an integer.
- The fix? __typecasting__, wrapping input() with _int()_ or _float()_.
- Use int() for whole numbers and float() when decimals are possible. This applies everywhere you take numeric input from a user.


## Useful Number Functions
- several built-in functions for working with numbers. _round(value,n)_ rounds to n decimal places: _round(3.14159,2)_ gives 3.14. abs(value) returns the absolute value(**removes the negative sign): abs(-7) gives 7**.

- This usedul when you care about the magnitude of a difference, not its direction. _int(), float(), and str() convert between types, these are your main type casting tools._


## Operator Precedence

- Python follows standard mathematical order of operations: brackets first, then exponents, then multiplication/division/modulus, then addition/subtraction.
- Memorise **BEDMAS**. When in doubt, add brackets:(2 + 3) * 4 = 20, whereas 2 + 3 * 4 = 14 because multiplicatoin happens before addition.