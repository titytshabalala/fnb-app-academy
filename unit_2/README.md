# Unit 2
## String Manipulation and Formatting

### Core lessons of the unit:
- Learn the essential techniques for working with text in Python.
- Explore how strings can be transformed, searched, measured and organized using built-in tools.
- Develop an ability to access and manipulate specific portions of text *with precision*.
- Learn to process and present text __effectively__ in Python programs.

## Learning Objectives
1. Apply string methods (**at least 7**)
2. Use *len()* to count characters in string
3. Access individual characters and substrings using **indexing** and **slicing**
4. Format output using *f-strings*
5. Concatenate strings using **+** and format them with *f-strings*

### String Methods:
- .upper() -> converts **ALL CAPS**
- .lower() -> converts to all lowercase
- .title() -> converts to Title Case
- .strip() -> removes leading and trailing whitespace
- .replace(old value, new value) -> swaps out one substring for another.
- .find(value) -> returns the index of the first occurence **if** not found -1 is returned.
- .split(delimeter) -> breaks (splits) a string into a list
- .len(string) returns the character count.


## Indexing and Slicing
- Every character in a string has a position number called an *index* starting at **0**.
- Slicing extracts a portion of the index value.
- Negative indexes count from **right to left**


## f-strings
- An f-string (formatted string literal) is the cleanest way to embed variables and expressions inside text.
- Prefix the string with f, then wrap any variable or expression in curly braces.
- Call methods, do arithmetic, and embed any Python expression inside the curly braces. f-strings replace older methods like *.format() and % formatting and are the preffered style in modern Python*