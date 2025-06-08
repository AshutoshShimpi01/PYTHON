Type	         Example	         Ordered?	  Mutable?	 Key-Value?    Duplicates

List	         [1, 2, 3]	          ✅	        ✅	        ❌        ✅	      
Dictionary	 {'a': 1, 'b': 2}	      ✅	        ✅	        ✅        ❌ (keys)
Set	          {1, 2, 3}	            ❌	        ✅	        ❌        ❌
Tuple        	(1, 2, 3)	            ✅	        ❌	        ❌        ✅

------------------------------------------------------------------------------------

Type	                  Example             	              Has :?	  Ordered?	  Good for DataFrame?
List of Dicts	 [{'name': 'Ashu', 'age': 24},{...}]	          ✅ Yes	   ✅ Yes	       ✅ Yes
List of Sets  	[{'Ashu', 24}, {'keshu', 19}]	                ❌ No      ❌ No	         ❌ No





#list of tuples 
data = [("Ashu",24),("keshu",19)]
col = ["Name","age"]
df = spark.createDataFrame(data,col)
df.show()


#list of dictionaries.
data = [{'id':1,'name':"Ashu"},{'id':2,'name':"keshu"}]
df = spark.createDataFrame(data)
df.show()

#we cannot use list of sets with dataFrame. its only take value not key.  (error occurs)


# Example: Tuple containing two lists
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'])







1. What is PySpark?
PySpark is the Python API for Apache Spark, an open-source, distributed computing system used for big data processing and analytics.

2. What is an RDD in PySpark?
RDD (Resilient Distributed Dataset) is the fundamental data structure in Spark. It's an immutable distributed collection of objects that can be processed in parallel.

3. What is the difference between RDD and DataFrame in PySpark?
RDD: Low-level, less optimized, good for complex operations.

DataFrame: High-level abstraction, optimized using Catalyst optimizer, similar to a table in SQL.

4. How do you create a DataFrame in PySpark?

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()
data = [("Alice", 1), ("Bob", 2)]
df = spark.createDataFrame(data, ["Name", "ID"])
df.show()
  
5. What is the use of show() and printSchema()?
show() displays the content of a DataFrame.

printSchema() prints the structure/schema of the DataFrame.

6. What are transformations and actions in PySpark?
Transformations (e.g., filter(), map(), select()): Lazy operations that define a new RDD/DataFrame.

Actions (e.g., show(), count(), collect()): Trigger execution and return results.

7. How do you filter data in a DataFrame?

df.filter(df["ID"] > 1).show()
                              
8. How do you group data in PySpark?

df.groupBy("Name").count().show()
                              
9. What is SparkSession and why is it used?
SparkSession is the entry point to programming with Spark. It allows the creation of DataFrames and execution of SQL queries.

10. How do you read a CSV file in PySpark?

df = spark.read.csv("file.csv", header=True, inferSchema=True)
df.show()
  
11. Read a JSON file

df = spark.read.json("data.json")
df.show()

12. Get distinct values from a column

df.select("Department").distinct().show()

13. Drop duplicate rows

df.dropDuplicates().show()

14. Replace null values

df.fillna("Unknown").show()

15. Filter rows with NULL in a specific column

df.filter(df["Age"].isNull()).show()

16. Cast a column to a different data type

df.withColumn("Salary", df["Salary"].cast("Integer")).printSchema()

17. Combine two columns into one

from pyspark.sql.functions import concat_ws

df.withColumn("FullName", concat_ws(" ", df["FirstName"], df["LastName"])).show()

18. Calculate average salary

from pyspark.sql.functions import avg

df.select(avg("Salary")).show()

19. Use SQL queries on DataFrame

df.createOrReplaceTempView("emp")
spark.sql("SELECT Department, COUNT(*) FROM emp GROUP BY Department").show()

20. Write DataFrame to CSV

df.write.csv("output/employees_output.csv", header=True)


Great! Here are PySpark join examples—very important for interviews and real-world data engineering work.

  
🔗 Joins in PySpark (with examples)
21. Inner Join
Join two DataFrames on a common column.

df1.join(df2, df1["id"] == df2["id"], "inner").show()
  
22. Left Join (Left Outer Join)
Returns all rows from the left DataFrame, and matching rows from the right.

df1.join(df2, df1["id"] == df2["id"], "left").show()

23. Right Join (Right Outer Join)
Returns all rows from the right DataFrame, and matching rows from the left.

df1.join(df2, df1["id"] == df2["id"], "right").show()

24. Full Outer Join
Returns all records when there is a match in either left or right.

df1.join(df2, df1["id"] == df2["id"], "outer").show()

25. Left Anti Join
Returns only rows from the left DataFrame that do not match in the right DataFrame.

df1.join(df2, df1["id"] == df2["id"], "left_anti").show()
  
26. Left Semi Join
Returns only rows from the left DataFrame that have a match in the right DataFrame (like WHERE EXISTS in SQL).

df1.join(df2, df1["id"] == df2["id"], "left_semi").show()

✅ Example Setup for Practice:

data1 = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
data2 = [(1, "HR"), (2, "Finance")]

df1 = spark.createDataFrame(data1, ["id", "name"])
df2 = spark.createDataFrame(data2, ["id", "department"])






You said:
10 basic coding questions


ChatGPT said:
Here are 10 Basic PySpark Coding Interview Questions (with examples) to help you prepare for entry-level roles or beginner rounds:

1. Read a CSV file into a DataFrame

df = spark.read.csv("employees.csv", header=True, inferSchema=True)
df.show()
  
2. Select specific columns from a DataFrame

df.select("Name", "Salary").show()

3. Filter rows where Salary > 50000

df.filter(df["Salary"] > 50000).show()

4. Count the number of rows in a DataFrame

print(df.count())

5. Group by Department and count employees

df.groupBy("Department").count().show()

6. Add a new column with a fixed value

from pyspark.sql.functions import lit

df.withColumn("Country", lit("India")).show()

7. Rename a column

df.withColumnRenamed("Name", "EmployeeName").show()

8. Drop a column

df.drop("Age").show()

9. Sort the DataFrame by Salary descending

df.orderBy(df["Salary"].desc()).show()
  
10. Create a new column with conditional logic (if-else)

from pyspark.sql.functions import when

df.withColumn("Status", when(df["Salary"] > 50000, "High").otherwise("Low")).show()
