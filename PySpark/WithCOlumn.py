Sample DataFrame:
Let's assume this is your input:


data = [("Alice", 23), ("Bob", 35), ("Charlie", 17)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)




✅ 1. Count comma-separated values (like your example)
python
Copy
Edit
from pyspark.sql.functions import split, size

df = spark.createDataFrame([("Amit", "30,130,20,4")], ["name", "marks"])
df_with_count = df.withColumn("Marks Count", size(split(df["marks"], ",")))
🟢 Counts how many values are in the comma-separated string.

✅ 2. Add constant value to a column
python
Copy
Edit
from pyspark.sql.functions import col

df = spark.createDataFrame([("Alice", 20)], ["name", "age"])
df = df.withColumn("age_plus_10", col("age") + 10)
--Same both
employees_df.withColumn("age_plus_10", employees_df.salary + 101).show()

🟢 Adds 10 to the age.

✅ 3. Create a new column with constant value
python
Copy
Edit
from pyspark.sql.functions import lit

df = df.withColumn("country", lit("India"))
🟢 Adds "India" as a constant value to all rows.

✅ 4. Classify using when (age group example)
python
Copy
Edit
from pyspark.sql.functions import when

df = df.withColumn(
    "age_group",
    when(col("age") < 18, "Minor")
    .when(col("age") < 60, "Adult")
    .otherwise("Senior")
)
🟢 Creates a category based on age.

✅ 5. Uppercase a column
python
Copy
Edit
from pyspark.sql.functions import upper

df = df.withColumn("name_upper", upper(col("name")))
🟢 Converts names to uppercase.

✅ 6. Length of a string column
python
Copy
Edit
from pyspark.sql.functions import length

df = df.withColumn("name_length", length(col("name")))
🟢 Calculates length of each name.

✅ 7. Extract part of string
python
Copy
Edit
from pyspark.sql.functions import substring

df = df.withColumn("first_letter", substring(col("name"), 1, 1))
🟢 Extracts first letter from name.

✅ 8. Boolean column based on condition
python
Copy
Edit
df = df.withColumn("is_adult", col("age") >= 18)
🟢 Creates True/False column if age ≥ 18.

✅ 9. Split a string into an array
python
Copy
Edit
df = df.withColumn("marks_array", split(col("marks"), ","))
🟢 Turns "30,130,20" → ["30", "130", "20"].

✅ 10. Round a numeric column
python
Copy
Edit
from pyspark.sql.functions import round

df = df.withColumn("rounded_age", round(col("age") / 3, 2))
🟢 Divides age by 3 and rounds to 2 decimal places.

