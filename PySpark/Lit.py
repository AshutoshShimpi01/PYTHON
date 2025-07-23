🔹 Why use lit()?
In PySpark, when you want to:

Add a new column with a constant value

Compare a column with a constant inside withColumn, select, or filter

You must wrap the constant value with lit(), because PySpark expects column expressions, not raw Python values.

✅ Example 1: Add a constant column

from pyspark.sql.functions import lit

df = df.withColumn("Country", lit("India"))
df.show()
🔸 This adds a new column Country with value "India" for every row.

✅ Example 2: Use lit() in conditions

from pyspark.sql.functions import col

df.filter(col("Salary") > lit(50000)).show()
🔸 You're comparing column Salary with constant 50000.
🔸 lit(50000) wraps the constant as a Column object, which Spark understands.

❌ What if you don’t use lit()?

df.withColumn("new_col", "India")  # ❌ ERROR!
You’ll get an error like:


TypeError: Column is not iterable
Because "India" is a Python string, not a Column object.

✅ Summary:
Use Case	Without lit()	With lit() ✅
Add constant value as column	❌ Error	✅ Works
Compare column with fixed number	❌ Error	✅ Works
