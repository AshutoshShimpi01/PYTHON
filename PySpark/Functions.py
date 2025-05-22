Sure! Here's a quick guide to basic and commonly used PySpark functions, especially for working with DataFrames — useful for beginners and practical day-to-day tasks.

✅ 1. Creating a DataFrame

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Basics").getOrCreate()

data = [("Ashu", 24), ("Keshu", 19)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()


✅ 2. Viewing Data
Function	Description
df.show()	Displays the top 20 rows
df.printSchema()	Prints the schema (column types)
df.head()	Returns the first row
df.take(3)	Returns the first 3 rows
df.columns	Returns a list of column names


✅ 3. Selecting & Filtering

df.select("Name").show()  # Select one column
df.select("Name", "Age").show()  # Select multiple columns

df.filter(df.Age > 20).show()  # Filter rows where age > 20
df.where(df.Name == "Ashu").show()  # Same as filter



✅ 4. Adding & Renaming Columns

from pyspark.sql.functions import col, lit

df.withColumn("Country", lit("India")).show()  # Add constant column

df.withColumn("AgePlus1", col("Age") + 1).show()  # Modify column

df.withColumnRenamed("Age", "Years").show()  # Rename column



✅ 5. Grouping and Aggregating

df.groupBy("Name").count().show()  # Group by name and count

from pyspark.sql.functions import avg, max, min

df.agg(avg("Age"), max("Age"), min("Age")).show()



✅ 6. Sorting and Distinct

df.sort("Age").show()  # Ascending
df.orderBy(df.Age.desc()).show()  # Descending

df.select("Age").distinct().show()  # Unique values



✅ 7. Joins

df1.join(df2, on="id", how="inner").show()
# Join types: inner, left, right, outer



✅ 8. Dropping & Replacing

df.drop("Age").show()  # Drop a column

df.na.drop().show()  # Drop rows with nulls
df.na.fill(0).show()  # Replace nulls with 0



✅ 9. Saving Data

df.write.csv("output.csv")  # Save to CSV
df.write.json("output.json")  # Save to JSON



✅ 10. SQL Queries (Optional but powerful)

df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE Age > 20").show()
