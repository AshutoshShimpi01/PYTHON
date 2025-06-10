Here are 20 commonly asked PySpark coding interview questions with explanations and sample code where relevant. 
These questions range from beginner to intermediate and are helpful for interviews related to data engineering or big data development roles.


    
🔹 1. How to create a DataFrame from a list or dictionary?

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Interview").getOrCreate()
data = [("John", 28), ("Sara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()


🔹 2. How to read a CSV file into a DataFrame?
 
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
df.show()


🔹 3. How to filter rows in a DataFrame?
 
df.filter(df.Age > 25).show()


🔹 4. How to select specific columns?
 
df.select("Name", "Age").show()


🔹 5. How to add a new column using withColumn?
 
from pyspark.sql.functions import col

df = df.withColumn("AgePlus10", col("Age") + 10)


🔹 6. How to rename a column?
 
df = df.withColumnRenamed("Age", "Years")


🔹 7. How to drop a column?
 
df = df.drop("Age")


🔹 8. How to group by and aggregate?
 
df.groupBy("Name").agg({"Age": "avg"}).show()


🔹 9. How to sort data in a DataFrame?
 
df.orderBy("Age", ascending=False).show()


🔹 10. How to join two DataFrames?
 
df1.join(df2, df1.id == df2.id, "inner").show()


🔹 11. How to get distinct values?
 
df.select("Name").distinct().show()


🔹 12. How to deal with nulls?
Drop rows with nulls:

 
df.na.drop().show()
Fill nulls:
 
df.na.fill({"Age": 0}).show()


🔹 13. How to use when and otherwise for conditional logic?
 
from pyspark.sql.functions import when

df = df.withColumn("Category", when(col("Age") > 25, "Senior").otherwise("Junior"))


🔹 14. How to use explode() on arrays?
 
from pyspark.sql.functions import explode

df = spark.createDataFrame([(["Python", "Spark"],)], ["Skills"])
df.select(explode(df.Skills)).show()


🔹 15. How to use pivot and unpivot?
 
df.groupBy("Name").pivot("Subject").agg({"Score": "avg"}).show()


🔹 16. How to cache/persist a DataFrame?
 
df.cache()
df.persist()


🔹 17. How to create a UDF (User Defined Function)?
 
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def upper_case(name):
    return name.upper()

upper_udf = udf(upper_case, StringType())
df = df.withColumn("UpperName", upper_udf(col("Name")))


🔹 18. How to write a DataFrame to a file (CSV/Parquet/JSON)?
 
df.write.csv("output.csv", header=True)
df.write.parquet("output.parquet")
df.write.json("output.json")


🔹 19. How to use window functions (e.g., row_number, rank)?
 
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("Department").orderBy("Salary")
df = df.withColumn("row_num", row_number().over(windowSpec))
🔹 20. How to read JSON and handle corrupt records?
 
df = spark.read.option("mode", "PERMISSIVE").option("columnNameOfCorruptRecord", "_corrupt_record").json("file.json")
df.show()


21. How to convert a DataFrame column to timestamp/date type?
 
from pyspark.sql.functions import to_date, to_timestamp

df = df.withColumn("Date", to_date(col("date_str"), "yyyy-MM-dd"))
df = df.withColumn("Timestamp", to_timestamp(col("timestamp_str"), "yyyy-MM-dd HH:mm:ss"))


🔹 22. How to repartition and coalesce a DataFrame?
 
# Repartition (increases or reshuffles partitions)
df = df.repartition(4)

# Coalesce (reduce partitions without shuffle)
df = df.coalesce(2)


🔹 23. How to remove duplicate rows from a DataFrame?
 
df = df.dropDuplicates()


🔹 24. How to get schema and DataFrame information?
 
df.printSchema()
df.describe().show()
df.summary().show()


🔹 25. How to flatten a nested JSON structure?
 
from pyspark.sql.functions import col

df = spark.read.json("nested.json")


df.select(col("employee.name"), col("employee.age")).show()
🔹 26. How to collect list of values per group (grouped collect)?
 
from pyspark.sql.functions import collect_list

df.groupBy("Department").agg(collect_list("Name").alias("Employees")).show()


🔹 27. How to broadcast a small DataFrame in join?
 
from pyspark.sql.functions import broadcast

df1.join(broadcast(df2), "id").show()
🔹 28. How to use isin() for multiple value filtering?
 
df.filter(df.Name.isin("John", "Sara")).show()


🔹 29. How to create a DataFrame schema manually?
 
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)


🔹 30. How to convert DataFrame to RDD and vice versa?
 
# DataFrame to RDD
rdd = df.rdd

# RDD to DataFrame
df2 = rdd.toDF(["Name", "Age"])
