Here are 20 commonly asked PySpark coding interview questions with explanations and sample code where relevant. 
These questions range from beginner to intermediate and are helpful for interviews related to data engineering or big data development roles.

🔹 1. How to create a DataFrame from a list or dictionary?
python
Copy
Edit
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Interview").getOrCreate()
data = [("John", 28), ("Sara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
🔹 2. How to read a CSV file into a DataFrame?
python
Copy
Edit
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
df.show()
🔹 3. How to filter rows in a DataFrame?
python
Copy
Edit
df.filter(df.Age > 25).show()
🔹 4. How to select specific columns?
python
Copy
Edit
df.select("Name", "Age").show()
🔹 5. How to add a new column using withColumn?
python
Copy
Edit
from pyspark.sql.functions import col

df = df.withColumn("AgePlus10", col("Age") + 10)
🔹 6. How to rename a column?
python
Copy
Edit
df = df.withColumnRenamed("Age", "Years")
🔹 7. How to drop a column?
python
Copy
Edit
df = df.drop("Age")
🔹 8. How to group by and aggregate?
python
Copy
Edit
df.groupBy("Name").agg({"Age": "avg"}).show()
🔹 9. How to sort data in a DataFrame?
python
Copy
Edit
df.orderBy("Age", ascending=False).show()
🔹 10. How to join two DataFrames?
python
Copy
Edit
df1.join(df2, df1.id == df2.id, "inner").show()
🔹 11. How to get distinct values?
python
Copy
Edit
df.select("Name").distinct().show()
🔹 12. How to deal with nulls?
Drop rows with nulls:

python
Copy
Edit
df.na.drop().show()
Fill nulls:

python
Copy
Edit
df.na.fill({"Age": 0}).show()
🔹 13. How to use when and otherwise for conditional logic?
python
Copy
Edit
from pyspark.sql.functions import when

df = df.withColumn("Category", when(col("Age") > 25, "Senior").otherwise("Junior"))
🔹 14. How to use explode() on arrays?
python
Copy
Edit
from pyspark.sql.functions import explode

df = spark.createDataFrame([(["Python", "Spark"],)], ["Skills"])
df.select(explode(df.Skills)).show()
🔹 15. How to use pivot and unpivot?
python
Copy
Edit
df.groupBy("Name").pivot("Subject").agg({"Score": "avg"}).show()
🔹 16. How to cache/persist a DataFrame?
python
Copy
Edit
df.cache()
df.persist()
🔹 17. How to create a UDF (User Defined Function)?
python
Copy
Edit
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def upper_case(name):
    return name.upper()

upper_udf = udf(upper_case, StringType())
df = df.withColumn("UpperName", upper_udf(col("Name")))
🔹 18. How to write a DataFrame to a file (CSV/Parquet/JSON)?
python
Copy
Edit
df.write.csv("output.csv", header=True)
df.write.parquet("output.parquet")
df.write.json("output.json")
🔹 19. How to use window functions (e.g., row_number, rank)?
python
Copy
Edit
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("Department").orderBy("Salary")
df = df.withColumn("row_num", row_number().over(windowSpec))
🔹 20. How to read JSON and handle corrupt records?
python
Copy
Edit
df = spark.read.option("mode", "PERMISSIVE").option("columnNameOfCorruptRecord", "_corrupt_record").json("file.json")
df.show()
