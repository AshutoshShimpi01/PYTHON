Here are 20 common Python interview questions for Data Engineer roles with their answers:

✅ 1. What are Python’s key features that make it suitable for data engineering?
Answer:

Easy syntax and readability

Strong support for data libraries (e.g., Pandas, NumPy, PySpark)

Integration with databases and cloud tools

Works well for automation and scripting

Cross-platform and open-source

✅ 2. What is the difference between a list, tuple, set, and dictionary?
Answer:

List: Ordered, mutable, allows duplicates ([])

Tuple: Ordered, immutable, allows duplicates (())

Set: Unordered, mutable, no duplicates (set())

Dictionary: Key-value pairs, unordered, mutable no duplicates({})

✅ 3. What is the difference between shallow copy and deep copy?
Answer:

Shallow copy creates a new object but references the same inner objects.

Deep copy recursively copies all nested objects.

import copy
shallow = copy.copy(original)
deep = copy.deepcopy(original)



✅ 4. Explain list comprehension with an example.
# Without list comprehension
squares = []
for i in range(5):
    squares.append(i*i)

# With list comprehension
squares = [i*i for i in range(5)]


✅ 5. What are lambda functions?
Answer:
Anonymous functions written in one line.

add = lambda x, y: x + y
add(3, 5)  # Output: 8


✅ 6. What are *args and **kwargs?
Answer:

*args: allows variable number of positional arguments

**kwargs: allows variable number of keyword arguments

def test(*args, **kwargs):
    print(args)
    print(kwargs)


✅ 7. What are generators?
Answer:
Generators return an iterator and use yield instead of return. They're memory efficient for large datasets.


def my_gen():
    for i in range(3):
        yield i


✅ 8. Difference between is and ==?
Answer:

== checks value equality

is checks object identity

a = [1,2]
b = a
a is b  # True
a == b  # True


✅ 9. How do you handle exceptions in Python?
Answer:

try:
    val = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")


✅ 10. What is GIL in Python?
Answer:
Global Interpreter Lock prevents multiple threads from executing Python bytecode simultaneously, limiting true multithreading in CPython.


✅ 11. How do you read/write large CSV files?
Answer:

import pandas as pd
df = pd.read_csv("data.csv", chunksize=10000)
for chunk in df:
    process(chunk)


✅ 12. Difference: read(), readline(), readlines()?
Answer:

read() - entire file as a string

readline() - one line at a time

readlines() - list of lines


✅ 13. Parse JSON into Python dict?
Answer:

import json
data = '{"name": "Ashu", "age": 25}'
parsed = json.loads(data)


✅ 14. Remove duplicates from a list?
Answer:

unique = list(set([1, 2, 2, 3]))


✅ 15. Count word frequency in a text file?
Answer:

from collections import Counter
with open("file.txt") as f:
    words = f.read().split()
    count = Counter(words)


✅ 16. Useful Pandas functions for ETL?
Answer:

read_csv(), to_csv()

dropna(), fillna()

groupby(), merge()

apply() for custom logic



✅ 17. PySpark example:
Answer:

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()
df = spark.read.csv("file.csv", header=True, inferSchema=True)
df.filter(df['age'] > 30).show()



✅ 18. map(), filter(), reduce()?
Answer:

from functools import reduce
nums = [1,2,3]
map_result = list(map(lambda x: x*2, nums))
filter_result = list(filter(lambda x: x > 1, nums))
reduce_result = reduce(lambda x, y: x + y, nums)


✅ 19. Connect to a database using Python?
Answer:

import psycopg2
conn = psycopg2.connect(host="localhost", dbname="test", user="user", password="pass")


✅ 20. What are pickle and json modules used for?
Answer:

pickle: serialize Python objects (binary)

json: serialize into human-readable JSON


✅ 21. What is the difference between apply() and map() in Pandas?
Answer:

map() is used with Series for element-wise transformations.

apply() works with both Series and DataFrames and can apply functions row-wise or column-wise.

df['col'].map(lambda x: x + 1)
df.apply(lambda row: row['col1'] + row['col2'], axis=1)



✅ 22. How do you handle missing values in a DataFrame?
Answer:

df.dropna() – drops missing rows

df.fillna(value) – fills missing with a value

df.isnull().sum() – counts missing values



✅ 23. What is a Python decorator?
Answer:
A function that modifies another function's behavior without changing its code.

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")


✅ 24. How do you merge DataFrames in Pandas?
Answer:

pd.merge(df1, df2, on='id', how='inner')  # types: inner, outer, left, right


✅ 25. What is a context manager in Python?
Answer:
Used with with statements to manage resources like files or DB connections.

with open('file.txt') as f:
    data = f.read()


✅ 26. What are Python's data serialization formats?
Answer:

JSON – human-readable

Pickle – Python object binary format

CSV / Parquet / Avro – common for data pipelines
  
  
✅ 27. Difference between iter() and next()?
Answer:

iter() returns an iterator object


✅ 28. What is the use of __init__ in a Python class?
Answer:
The constructor method used to initialize object properties.

class Person:
    def __init__(self, name):
        self.name = name


✅ 29. How do you schedule Python ETL jobs?
Answer:

Use Apache Airflow, cron, or cloud schedulers.

Python’s schedule module can also be used for simple tasks.



✅ 30. What are best practices for writing Python code in production?
Answer:

Use virtual environments

Modularize code

Use logging instead of print

Handle exceptions

Write unit tests

Follow PEP 8 style guide

next() fetches the next element in the iterator
