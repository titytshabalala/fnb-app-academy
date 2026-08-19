# unit 5
## Conditional Logic and Decision Making
- understanding the principles of decision-making in Python, allowing programs to repond differently based on specific conditions.
- learning how logical comparisons guide the flow of program execution.
- explore how multiple conditions can be combined to create more flexible and meaningful outcomes.
- Discover how Python evaluates membership and interprets different values in conditional statements.

## Learning Objectives
1. Write if, elif, and else statements to control program flow based on conditions.
2. Use comparison operators *(==, !=, <,>, <=,>=)* correctly in conditions.
3. Combine conditions using logical operators: *and, or, not*
4. Use the **in** keyword to check membership in a *list or string*
5. Nest conditional statements where appropriate and explain when to use elif vs separate if.




## Selection of Tasks
### Conditional Logic
Without conditional logic, every program runs the same way every time regardless of input.
- Conditionals let your program **make decisions**
- Python checks each condition in *order* and executes the first block where the condition is **True**.
- **elif (if-else)** chains multiple conditions.
- The else block is the fallback, it runs when all other conditions are **False**.
- **Indentation** is not optional, it is how Python knows which code belongs to which condition.

### Comparison Operators
- Six comparison operators return True or False: *== (equal to), != (not equal to), >(greater than), <(less than), >=(greater than or equal to), <=(less than or equal to)*.
- A single *=* is assignment *(age = 22)*.
- A double *==* is comparison *(age == 22)*.
- Confusing the two, is one of the most common bugs in beginner code.


### Logical Operators
- Three logical operators combine conditions: **and: both conditions must be _True_**. **or: at least one condition must be _True_**. **not: inverts the result (True becomes False, False becomes True)**.
- Logical operators are evaluated after comparison operators, no brackets needed in most cases, but they improve readability.


### They **in** Keyword and Truthiness

- The **in** keyword checks membership: *if 'admin' in roles checks whether 'admin' is in the roles list*.
- It workds on strings too: *if '@' in email checks for a valid email format*.
- Python also has a concept of **truthiness**, empty strings, 0, None, and empty lists are all falsy.
- Meaning if username: is a valid check for whether a string is non-empty.

