That's a broad request\! To give you a good starting point, here are five **basic Python scripts** covering essential concepts like input/output, math, conditionals, loops, and data structures.

You can run all of these scripts directly in a Python interpreter.

-----

## 1\. Simple Calculator (Input/Output and Basic Math)

This script takes two numbers and performs basic arithmetic.

```python
# Script 1: Simple Calculator
print("--- Simple Calculator ---")

# Get input from the user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Use an if-else condition to handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Print results
print(f"\nResults for {num1} and {num2}:")
print(f"  Addition: {addition}")
print(f"  Subtraction: {subtraction}")
print(f"  Multiplication: {multiplication}")
print(f"  Division: {division}")
```

-----

## 2\. Even or Odd Checker (Conditionals and Modulo)

This script uses the modulo operator (`%`) to determine if a number is even or odd.

```python
# Script 2: Even or Odd Checker
print("--- Even or Odd Checker ---")

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# The core logic: check the remainder when divided by 2
if number % 2 == 0:
    print(f"The number {number} is **Even**.")
else:
    print(f"The number {number} is **Odd**.")
```

-----

## 3\. Countdown Timer (Loops and `range()`)

This script uses a `for` loop and the `range()` function with a negative step to count backward.

```python
# Script 3: Simple Countdown Timer
import time # Import the time module to pause execution

print("--- 5 Second Countdown ---")

# Loop from 5 down to 1 (stop before 0), step by -1
for i in range(5, 0, -1):
    print(i)
    time.sleep(1) # Pause the script for 1 second

print("LIFT OFF!")
```

-----

## 4\. List Operations (Loops and Lists)

This script demonstrates iterating over a list and performing an operation (squaring) on its elements.

```python
# Script 4: List Operations (Squaring Elements)
print("--- List Operations ---")

initial_list = [1, 2, 3, 4, 5]
squared_list = []

print(f"Initial List: {initial_list}")

# Use a for loop to process each item
for item in initial_list:
    # Calculate the square (item multiplied by itself)
    square = item ** 2 
    # Add the result to the new list
    squared_list.append(square)

print(f"Squared List: {squared_list}") 
# Note: A more "Pythonic" way to do this is with a list comprehension:
# squared_list = [item ** 2 for item in initial_list]
```

-----

## 5\. Basic Character Counter (Dictionaries/`Counter`)

This script counts the total frequency of each character in an input string.

```python
# Script 5: Basic Character Counter
from collections import Counter

print("--- Character Frequency Counter ---")
text = input("Enter a word or phrase: ").lower().replace(" ", "")

if not text:
    print("No input provided.")
else:
    # Use the Counter class to efficiently count frequencies
    counts = Counter(text)
    
    print("\nCharacter Counts:")
    # Iterate over the key-value pairs (character and its count)
    for char, count in sorted(counts.items()):
        print(f"  '{char}': {count} times")
```
