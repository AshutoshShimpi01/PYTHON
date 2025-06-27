Common Ways to Use .select() in PySpark
🔹 1. Select All Columns
python
Copy
Edit
df.select("*")
Equivalent to SELECT * FROM table.

🔹 2. Select Specific Columns
python
Copy
Edit
df.select("column1", "column2")
Selects only those columns.

🔹 3. Select with Aliasing
python
Copy
Edit
from pyspark.sql.functions import col

df.select(col("column1").alias("new_name"))
Renames the column in the result.

🔹 4. Apply Functions to Columns
python
Copy
Edit
from pyspark.sql.functions import upper, length

df.select(upper("name").alias("UPPER_NAME"), length("name").alias("name_length"))
Applies transformations like UPPER() or LENGTH().

🔹 5. Select with Conditional Expressions
python
Copy
Edit
from pyspark.sql.functions import when

df.select("name", when(df.age > 18, "Adult").otherwise("Minor").alias("category"))
🔹 6. Select with Arithmetic Operations
python
Copy
Edit
df.select((df.salary * 0.10).alias("bonus"))
🔹 7. Select Nested or Struct Columns
python
Copy
Edit
df.select("person.name", "person.age")
If your DataFrame has a nested struct like person, you can access its fields like this.

🔹 8. Select using Expressions
python
Copy
Edit
df.selectExpr("name", "age * 2 as double_age")
selectExpr is like writing raw SQL expressions inside .select().

🧠 Tip:
Use .select() for transformations.

Use .withColumn() when you're adding/modifying columns.

