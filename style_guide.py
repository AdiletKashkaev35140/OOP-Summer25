
# Naming Conventions
# Use descriptive variable names in snake_case

# Correct
user_name = "John Doe"
order_total = 100.50

# Wrong
UserName = "John Doe"  # CamelCase is for classes
ordertotal = 100.50  # No separation between words

# Use 4 spaces per indentation level

def process_order(order):
    if order:
        print("Processing order...")
    else:
        print("No order to process.")

# Wrong

def wrong_indentation(order):
  if order:  # Only 2 spaces instead of 4
    print("Incorrect indentation")

# Keep lines to a maximum of 79 characters for readability

# Correct
def calculate_discount(price, discount_rate):
    return price - (price * discount_rate)

# Wrong

def long_function_with_too_many_parameters(price, discount_rate, tax_rate, shipping_fee, handling_fee, membership_discount):
    return price - (price * discount_rate) + tax_rate + shipping_fee + handling_fee - membership_discount  # Line too long

# Imports should be on separate lines and grouped logically

# Correct
import os
import sys
from datetime import datetime

# Wrong
import os, sys  # Multiple imports on one line
from datetime import datetime, time  # Unnecessary multiple imports from the same module

# Use proper spacing around operators and after commas

# Correct
x = 10 + 5
numbers = [1, 2, 3, 4]

# Wrong
x=10+5  # No spaces around operators
numbers=[1,2,3,4]  # No spaces after commas

# Use docstrings for modules, classes, and functions. Use comments sparingly but effectively.

# Correct
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Wrong
def greet_wrong(name):
    # This function greets the user
    return f"Hello, {name}!"  # Comment is redundant





