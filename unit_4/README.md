# Unit 4
## Introduction to Storage and Access
- Python's core data structures for organising and managing collections of information.
- Exploring how different structures store, retrieve, and organise data to suit different programming needs.
- Learn to develop an understanding of mutable (change/updatable) and immutable (cannot be changed once created) data and when *each is appropriate*.
- Learn to process structured data efficiently using iteration.
- These concepts provide the foundation for working with real-world datasets and buliding more sophisticated Python **applications**.

## Objectives:
1. Create and manipulate **lists** using indexing, append, remove, insert, and slicing.
2. Create and use **dictionaries** with key-value pairs using .get(), .keys(), .values(), and .items()
3. Explain the difference between mutable and immutable data types.
4. Bulid a **list of dictionaries** to represent structured collections of **real-world data**
5. Iterate over lists and dictionaries using *for loops*



## Terms explained
### Lists
- An ordered, mutable collection of values stored in a single variable.
- Created using *[]*  square brackets
- Items of a list are accessed using an index (0,1,2,...)
- Negative indexes count from the end.
- **List methods**: *.append(item) adds to the end of the list; .insert(index,item) inserts at a position; .remove(item) removes by value; .pop(index) removes by index and returns the item; len(list) returns the count*.

### Dictionaries
- Dictionary stores key-value pairs.
- Think of it as a lookup table where every piece of adata has a name.
- Created using *{}* curly braces.
- Can access values by key: *contant[\'name\']*.
- Use .get(key) for safe access *which returns None instead of crashing if the key does not exist*.
- **Key methods**: *.keys() returns all keys; .values() returns all values; .items() returns (key,value) pairs for iteration*

### List of Dictionaries
- One of the most powerful data pattern in Python is a list of dictionaries.
- Each dictionary represents one record *(a contact, a student, a product)*, and the list holds all the records.
- This is how databases query results and API responses are structured - **JSON** responses from web APIs are nearly always lists of dictionaries.
- Iterating over this structure with a for loop lets you process every record in a few lines of code.

### Tuples: Immutable lists
- A tuple is like a list but immutable, meaning once created, **it cannot be changed**.
- Created with *()* parenthesis
- Use tuples when the data should not change, e.g GPS coordinates, RGB color values, days of the week.
- Attempting to modify a tuple raises a *TypeError*.