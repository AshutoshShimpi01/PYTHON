🧺 What is a list?
A list is a collection of items — like a box of tools.
List – Ordered, changeable, allows duplicates

Add items:
tools.append("Spark")

Remove items:
tools.remove("SQL")


tools = ["Python", "SQL", "Airflow"]
print(tools)

-------------

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # add to list
print(fruits[0])         # first item

----------------

skills = ["Python", "SQL"]

skills.append("Airflow")

for skill in skills:
    print(skill)
OUT-    
Python
SQL
Airflow

-------------------
