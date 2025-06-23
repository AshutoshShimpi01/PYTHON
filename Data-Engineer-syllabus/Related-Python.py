Part 1: Basic Python Fundamentals
🔹 1. Variables and Data Types
python
Copy
Edit
x = 10          # Integer
name = "Ashu"   # String
price = 99.99   # Float
is_valid = True # Boolean
🔹 2. Lists, Tuples, Dictionaries
python
Copy
Edit
# List (mutable)
fruits = ['apple', 'banana', 'mango']

# Tuple (immutable)
colors = ('red', 'green', 'blue')

# Dictionary (key-value pair)
person = {'name': 'Ashu', 'age': 25}
🔹 3. Control Flow
python
Copy
Edit
# if-else
if x > 5:
    print("Greater")
else:
    print("Smaller")

# for loop
for fruit in fruits:
    print(fruit)

# while loop
count = 0
while count < 3:
    print(count)
    count += 1
🔹 4. Functions
python
Copy
Edit
def greet(name):
    return f"Hello, {name}!"

print(greet("Ashu"))
📦 Part 2: NumPy (Numerical Python)
NumPy is used for fast numerical operations, especially with arrays.

🔹 1. Creating Arrays
python
Copy
Edit
import numpy as np

arr = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
🔹 2. Useful Methods
python
Copy
Edit
np.zeros((2, 3))        # 2x3 matrix of zeros
np.ones((2, 3))         # 2x3 matrix of ones
np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)    # [0. , 0.25, 0.5, 0.75, 1.]
🔹 3. Array Operations
python
Copy
Edit
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b         # [5 7 9]
a * b         # [4 10 18]
a.mean()      # 2.0
a.shape       # (3,)
🐼 Part 3: Pandas (Data Manipulation)
Pandas is used for data analysis and manipulation using DataFrames and Series.

🔹 1. Importing Pandas
python
Copy
Edit
import pandas as pd
🔹 2. Creating DataFrame
python
Copy
Edit
data = {'Name': ['Ashu', 'Sara'], 'Age': [25, 22]}
df = pd.DataFrame(data)
🔹 3. Reading and Writing Files
python
Copy
Edit
pd.read_csv("file.csv")
df.to_csv("output.csv", index=False)
🔹 4. Exploring Data
python
Copy
Edit
df.head()         # First 5 rows
df.info()         # DataFrame structure
df.describe()     # Stats summary
df['Age']         # Select a column
df[['Name','Age']]# Select multiple columns
🔹 5. Filtering and Conditions
python
Copy
Edit
df[df['Age'] > 23]
🔹 6. Grouping and Aggregation
python
Copy
Edit
df.groupby('Name').mean()
