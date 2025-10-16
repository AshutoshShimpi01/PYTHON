Example: Join 3 Tables
Let’s say we have these DataFrames:

employees with columns: emp_id, name, dept_id

departments with columns: dept_id, dept_name

projects with columns: emp_id, project_name

🔗 Join Logic:
Join employees with departments on dept_id

Then join the result with projects on emp_id



--Same with my logic

emp_dept = employees.join(departments, 'dept_id')
final_df = emp_dept.join(projects, 'emp_id')
final_df.show()

--for left & right join

emp_dept = employees.join(departments, 'dept_id', 'left')
final_df = emp_dept.join(projects, 'emp_id', 'right')

emp_dept.show()
final_df.show()

----------------------


from pyspark.sql.functions import *

# Step 1: Join employees and departments
emp_dept = employees.join(departments, on='dept_id', how='inner')

# Step 2: Join the result with projects
final_df = emp_dept.join(projects, on='emp_id', how='inner')

final_df.show()



🧠 Tip:
If the column names you're joining on are different, you can do:

df1.join(df2, df1["id"] == df2["user_id"], how="inner")
And then .drop() one of the duplicate columns if needed.



------------------

How to find Employees without Managers?
from pyspark.sql.functions import col

# Left join employees with themselves on manager ID
emp_mgr_join = employees_df.alias('e').join(
    employees_df.alias('m'),
    col('e.mgr_id') == col('m.emp_id'),
    how='left'
)

# Filter employees where manager info is NULL (i.e., no matching manager)
employees_without_managers = emp_mgr_join.filter(col('m.emp_id').isNull()).select('e.emp_id', 'e.name')

employees_without_managers.show()

