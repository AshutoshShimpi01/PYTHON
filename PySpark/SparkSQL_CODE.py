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




✅ 1. Show all employee records

employees.show()


✅ 2. Select only employee names and salaries

employees.select("name", "salary").show()


✅ 3. Filter employees with salary > 55000

employees.filter(col("salary") > 55000).show()


✅ 4. Add a new column bonus = 10% of salary

employees.withColumn("bonus", col("salary") * 0.10).show()


✅ 5. Show employees from department 101 only

employees.filter(col("dept_id") == 101).show()


✅ 6. Sort employees by salary descending

employees.orderBy(col("salary").desc()).show()


✅ 7. Join employees with departments to show dept_name

employees.join(departments, on="dept_id", how="left").select("name", "dept_name").show()


✅ 8. Group by dept_id and find average salary

employees.groupBy("dept_id").agg(avg("salary").alias("avg_salary")).show()


✅ 9. Find number of employees in each department

employees.groupBy("dept_id").count().show()


✅ 10. Rename column name to employee_name

employees.withColumnRenamed("name", "employee_name").show()


✅ 11. Replace null department with value 999

employees.fillna({"dept_id": 999}).show()


✅ 12. Categorize employees by salary

employees.withColumn(
    "salary_band",
    when(col("salary") > 65000, "High")
    .when(col("salary") >= 50000, "Medium")
    .otherwise("Low")
).select("name", "salary", "salary_band").show()


✅ 13. Check if any department has more than 1 employee

employees.groupBy("dept_id").count().filter(col("count") > 1).show()


✅ 14. Add a constant column country with value 'India'

employees.withColumn("country", lit("India")).show()


✅ 15. Show employees who are not assigned to any department

employees.filter(col("dept_id").isNull()).show()







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








Step 2: 15 Intermediate PySpark Join Questions & Answers

🔹 1. Show all employees and their project names (if any)

employees.join(projects, on="emp_id", how="left")\
    .select("name", "project_name").show()


🔹 2. Show only employees who are working on at least one project

employees.join(projects, on="emp_id", how="inner")\
    .select("name", "project_name").distinct().show()


🔹 3. Show employees who are not assigned to any project

employees.join(projects, on="emp_id", how="left_anti").show()


🔹 4. Show departments and their employees (include departments with no employees)

departments.join(employees, on="dept_id", how="left")\
    .select("dept_name", "name").show()


🔹 5. Total hours worked per employee

projects.groupBy("emp_id")\
    .agg(sum("hours_worked").alias("total_hours"))\
    .join(employees, on="emp_id")\
    .select("name", "total_hours").show()


🔹 6. Join all 3 tables and show: employee name, department name, project name

employees.join(departments, "dept_id", "left")\
    .join(projects, "emp_id", "left")\
    .select("name", "dept_name", "project_name").show()


🔹 7. List employees working more than 100 hours on any project

projects.filter(col("hours_worked") > 100)\
    .join(employees, "emp_id")\
    .select("name", "project_name", "hours_worked").show()


🔹 8. Show each department and total salary of its employees

employees.groupBy("dept_id")\
    .agg(sum("salary").alias("total_salary"))\
    .join(departments, "dept_id")\
    .select("dept_name", "total_salary").show()


🔹 9. Show employee name and number of projects assigned

projects.groupBy("emp_id")\
    .agg(count("*").alias("project_count"))\
    .join(employees, "emp_id")\
    .select("name", "project_count").show()


🔹 10. Employees with more than one project

projects.groupBy("emp_id")\
    .agg(count("*").alias("project_count"))\
    .filter(col("project_count") > 1)\
    .join(employees, "emp_id")\
    .select("name", "project_count").show()


🔹 11. Latest project per employee (using window functions)

from pyspark.sql.window import Window

window_spec = Window.partitionBy("emp_id").orderBy(col("start_date").desc())

projects.withColumn("rn", row_number().over(window_spec))\
    .filter(col("rn") == 1)\
    .join(employees, "emp_id")\
    .select("name", "project_name", "start_date").show()


🔹 12. Which employees are in the Finance department and working on any project

emp_finance = employees.join(departments, "dept_id")\
    .filter(col("dept_name") == "Finance")

emp_finance.join(projects, "emp_id").select("name", "project_name").show()


🔹 13. Count of employees per department (including departments with no employees)

departments.join(employees, "dept_id", "left")\
    .groupBy("dept_name")\
    .agg(count("emp_id").alias("employee_count"))\
    .show()


🔹 14. Total hours worked on projects by department

employees.join(projects, "emp_id")\
    .groupBy("dept_id")\
    .agg(sum("hours_worked").alias("total_hours"))\
    .join(departments, "dept_id")\
    .select("dept_name", "total_hours").show()


🔹 15. List of employees with department name and total hours (even if 0)

emp_proj = employees.join(projects, "emp_id", "left")\
    .groupBy("emp_id", "name", "dept_id")\
    .agg(coalesce(sum("hours_worked"), lit(0)).alias("total_hours"))

emp_proj.join(departments, "dept_id", "left")\
    .select("name", "dept_name", "total_hours").show()





