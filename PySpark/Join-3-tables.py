Example: Join 3 Tables
Let’s say we have these DataFrames:

employees with columns: emp_id, name, dept_id

departments with columns: dept_id, dept_name

projects with columns: emp_id, project_name

🔗 Join Logic:
Join employees with departments on dept_id

Then join the result with projects on emp_id



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
