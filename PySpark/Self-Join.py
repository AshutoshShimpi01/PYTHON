from pyspark.sql.functions import *

df1 = employees.alias("e1")
df2 = employees.alias("e2")

result = df1.join(df2, df1["manager_id"] == df2["emp_id"], "inner")
result.select("e1.emp_id", "e1.name", "e2.name").show()



Explaination-

# Assume employees DataFrame has columns: emp_id, name, manager_id
emp1 = employees.alias("e1")  # employees
emp2 = employees.alias("e2")  # managers

# Self join where e1.manager_id == e2.emp_id
self_joined_df = emp1.join(emp2, emp1.manager_id == emp2.emp_id, "left")

# Select employee name and their manager name
self_joined_df.select(
    col("e1.emp_id").alias("employee_id"),
    col("e1.name").alias("employee_name"),
    col("e2.name").alias("manager_name")
).show()
