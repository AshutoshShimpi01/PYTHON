from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Basics of PySpark") \
    .master("local[*]") \
    .getOrCreate()


--To Create data frame

data = [("Ashu",24),("yogu",28),("shri",21),("Keshu",19)]
column = ["Name","age"]

df = spark.createDataFrame(data,column)
df.show

+-----+---+
| Name|age|
+-----+---+
| Ashu| 24|
| yogu| 28|
| shri| 21|
|Keshu| 19|
+-----+---+


--df.printSchema()
root
 |-- Name: string (nullable = true)
 |-- age: long (nullable = true)


 --df.select("Name").show()
 +-----+
| Name|
+-----+
| Ashu|
| yogu|
| shri|
|Keshu|


df.filter(df.age > 20).show()
+----+---+
|Name|age|
+----+---+
|Ashu| 24|
|yogu| 28|
|shri| 21|
+----+---+


df.withColumn("Age_in_5_years", df.age + 2).show()
+-----+---+--------------+
| Name|age|Age_in_5_years|
+-----+---+--------------+
| Ashu| 24|            26|
| yogu| 28|            30|
| shri| 21|            23|
|Keshu| 19|            21|
+-----+---+--------------+


df.groupBy("age").count().show()
+---+-----+
|age|count|
+---+-----+
| 24|    1|
| 28|    1|
| 21|    1|
| 19|    1|
+---+-----+



df.createOrReplaceTempView("people")

# Now run SQL query
result = spark.sql("SELECT Name, Age FROM people WHERE Age > 20")
+----+---+
|Name|Age|
+----+---+
|Ashu| 24|
|yogu| 28|
|shri| 21|
+----+---+
result.show()
