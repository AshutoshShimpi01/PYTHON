Your script has the right intention, but there are several syntax and logical issues. Below is the corrected and working version of your PySpark code based on the task 
description.

Question 1 : csv file - product_id, product_category, Price
File is in S3
explicitily define the schema, dont want to infer the schema
increase the price by 10% where category is "ABC"
habdle null values 
write the processed file into table


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col, when

# Step 1: Create SparkSession
spark = SparkSession.builder \
    .appName("app_spark") \
    .getOrCreate()

# Step 2: Define Schema Explicitly (no inferring)
schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("product_category", StringType(), True),
    StructField("price", IntegerType(), True)
])

# Step 3: Read CSV file from S3 with explicit schema and handle null values
df = spark.read.format("csv") \
    .schema(schema) \
    .option("header", "true") \
    .load("s3://your-bucket-name/your-file.csv") \
    .na.fill(0)  # Fill nulls with 0

# Step 4: Increase price by 10% for "ABC" category
df_updated = df.withColumn(
    "price",
    when(col("product_category") == "ABC", col("price") * 1.10).otherwise(col("price"))
)

# Step 5: Write to a table or Parquet file (e.g., to HDFS or managed table location)
df_updated.write \
    .mode("overwrite") \
    .format("parquet") \
    .save("hdfs://your-hdfs-path/final_price_table")







To solve this in PySpark, we will:
Split the comma-separated values in the Marks column into an array using split()
Count the number of elements in the array using size()

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, size

# Create Spark session
spark = SparkSession.builder.appName("Marks Count").getOrCreate()

# Sample data
data = [("Amit", "30,130,20,4"),
        ("Sukruta", "100,20,30"),
        ("Sonali", "140,10")]

columns = ["Student Name", "Marks"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Calculate count of comma-separated values
df_with_count = df.withColumn("Marks Count", size(split(df["Marks"], ",")))

# Show the result
df_with_count.select("Student Name", "Marks Count").show()






To achieve the desired result using SQL (e.g. with Spark SQL or in any SQL engine that supports string functions),
you need to count the number of comma-separated values in the Marks column.

SQL
----
SELECT 
  student_name,
  size(split(Marks, ',')) AS marks_count
FROM 
  students_info;
-----------------------
SparkSQL-

# Register the DataFrame as a temp view
df.createOrReplaceTempView("students_info")

# Run SQL
result = spark.sql("""
    SELECT 
        `Student Name` AS student_name,
        size(split(Marks, ',')) AS marks_count
    FROM students_info
""")

result.show()



      

Question 4 : Given a table Employee in which we have DeptId for each employee. Write a single SQL query to move the employees from DeptID 1 to 2 and move
employees from DeptId 2 to 1
     

UPDATE Employee
SET DeptId = CASE 
                WHEN DeptId = 1 THEN 2
                WHEN DeptId = 2 THEN 1
                ELSE DeptId
            END;



  
Question 5 : Write SQL Query to get Employee Name, Manager ID and number of employees in the department?
Given Employee Table:


SELECT 
    E1.Name, 
    E1.MGR_ID, 
    (SELECT COUNT(*) 
     FROM EmployeeInfo E2 
     WHERE E2.DeptId = E1.DeptId) AS Dep_EMP_Count
FROM EmployeeInfo E1;





You're trying to insert only new employees (i.e. those who do not already exist in Employee_final_table) from Employee_daily into Employee_final_table. 
The SQL query you wrote is almost correct, but the syntax has a few issues.


INSERT INTO Employee_final_table (name, address, email_id, start_date, end_date)
SELECT 
    d.name, 
    d.address, 
    d.email_id, 
    CURRENT_DATE, 
    NULL
FROM Employee_daily d
LEFT JOIN Employee_final_table f ON d.id = f.id
WHERE f.id IS NULL;



  


  
  
  
  



