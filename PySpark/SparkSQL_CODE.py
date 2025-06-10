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







spark.sql("SELECT * FROM employees").show()


SELECT name, salary FROM employees


SELECT * FROM employees WHERE salary > 55000


SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id


SELECT e.name, d.dept_name FROM employees e
JOIN departments d ON e.dept_id = d.dept_id


SELECT * FROM employees ORDER BY salary DESC


SELECT COUNT(*) AS total_employees, MAX(salary) AS max_salary FROM employees






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












