#Exception Handling is defined as the process of responding to the occurrence, during computation, 
# of exceptions – anomalous or exceptional conditions requiring special processing – often changing 
# the normal flow of program execution.


#difference between error and exception:
# An error is a more serious issue that typically cannot be handled programmatically,
# such as syntax errors or system-level failures.

# An exception is a condition that interrupts the normal flow of execution and can be 
# caught and handled in code.


# -------------------------------------------------
# EXCEPTION HANDLING IN PYTHON  
# -------------------------------------------------
"""
Definition:
Exception handling in Python is a mechanism that allows developers to manage errors and exceptional 
conditions gracefully during program execution. It helps maintain the normal flow of the program even
when unexpected situations arise.
Python provides built-in keywords such as try, except, else, finally, and raise to handle exceptions effectively.
Syntax:
    try:
        # Code that may raise an exception
    except ExceptionType1:
        # Code to handle ExceptionType1
    except ExceptionType2:
        # Code to handle ExceptionType2
    else:
        # Code to execute if no exceptions occur
    finally:
        # Code that will always execute, regardless of exceptions
"""
# -------------------------------------------------
# EXAMPLE OF EXCEPTION HANDLING 
# -------------------------------------------------
# Example 1: Handling Division by Zero Exception

try:
    n = int(input("Enter numerator: "))
    result = 10/n
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print(f"Result: {result}")  
finally:
    print("Execution completed.")   
# -------------------------------------------------
# END OF PROGRAM