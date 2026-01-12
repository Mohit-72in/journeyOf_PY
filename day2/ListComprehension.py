# Define Syntax of List Comprehension

# Syntax:
#     [expression for item in iterable if condition] or
#     [expression for item in iterable]
#     [expression if condition else alternative for item in iterable]
# Examples:
# 1. Basic List Comprehension 
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. List Comprehension with Condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# 3. List Comprehension with Else Condition
status = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(status)  # Output: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# 4. Nested List Comprehension    
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

strings = ["apple", "banana", "cherry"]
uppercase_strings = [s.upper() for s in strings]
print(uppercase_strings)  # Output: ['APPLE', 'BANANA', 'CHERRY']   
# -------------------------------------------------
# END OF PROGRAM
# ------------------------------------------------- 