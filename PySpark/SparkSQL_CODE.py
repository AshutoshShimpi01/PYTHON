from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create SparkSession
spark = SparkSession.builder.appName("SparkSQLPractice").getOrCreate()

# Employee Data
emp_data = [
    (1, "Alice", 30, 60000, 101),
    (2, "Bob", 40, 70000, 102),
    (3, "Charlie", 25, 50000, 101),
    (4, "David", 35, 55000, 103),
    (5, "Eva", 28, 48000, None)
]
emp_columns = ["emp_id", "name", "age", "salary", "dept_id"]
employees = spark.createDataFrame(emp_data, emp_columns)

# Department Data
dept_data = [
    (101, "HR"),
    (102, "Finance"),
    (103, "IT")
]
dept_columns = ["dept_id", "dept_name"]
departments = spark.createDataFrame(dept_data, dept_columns)

# Create temporary views for SQL
employees.createOrReplaceTempView("employees")
departments.createOrReplaceTempView("departments")



Add 3rd table--

from pyspark.sql.types import DateType

project_data = [
    (201, 1, "Billing System", 120, "2024-01-01"),
    (202, 2, "HRMS Upgrade", 150, "2024-02-10"),
    (203, 3, "Chatbot", 90, "2024-03-05"),
    (204, 1, "Compliance App", 60, "2024-04-01"),
    (205, 4, "IT Infra Setup", 80, "2024-01-20")
]
project_columns = ["project_id", "emp_id", "project_name", "hours_worked", "start_date"]
projects = spark.createDataFrame(project_data, project_columns)\
    .withColumn("start_date", col("start_date").cast(DateType()))

projects.createOrReplaceTempView("projects")




 1. Show all employees

employees.show()


🔹 2. Filter employees with salary > 55000

employees.filter(col("salary") > 55000).show()


🔹 3. Group by department and find average salary

employees.groupBy("dept_id").agg(avg("salary").alias("avg_salary")).show()


🔹 4. Join employees with departments

employees.join(departments, on="dept_id", how="left").select("name", "dept_name").show()


🔹 5. Join employees with projects and show hours worked

employees.join(projects, on="emp_id").select("name", "project_name", "hours_worked").show()


🔹 6. Categorize employees by salary using when

employees.withColumn(
    "salary_level",
    when(col("salary") >= 65000, "High")
    .when(col("salary") >= 50000, "Medium")
    .otherwise("Low")
).show()


🔹 7. Employees who worked more than 100 hours on any project

projects.filter(col("hours_worked") > 100)\
    .join(employees, on="emp_id")\
    .select("name", "project_name", "hours_worked").show()


🔹 8. Employees with no project (anti join)

employees.join(projects, on="emp_id", how="left_anti").show()

projects.groupBy("emp_id").agg(count("*").alias("project_count"))\
    .join(employees, on="emp_id")\
    .select("name", "project_count").show()


🔹 10. Most recent project per employee (Window Function)

from pyspark.sql.window import Window

window_spec = Window.partitionBy("emp_id").orderBy(col("start_date").desc())

projects.withColumn("row_num", row_number().over(window_spec))\
    .filter(col("row_num") == 1)\
    .select("emp_id", "project_name", "start_date")\
    .join(employees, on="emp_id")\
    .select("name", "project_name", "start_date").show()










