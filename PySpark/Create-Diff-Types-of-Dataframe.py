| Source Type      | Code Example                       |
| ---------------- | ---------------------------------- |
| List of Tuples   | `createDataFrame(data, columns)`   |
| List of Dicts    | `createDataFrame(data)`            |
| Pandas DataFrame | `createDataFrame(pandas_df)`       |
| RDD              | `createDataFrame(rdd)`             |
| Explicit Schema  | `createDataFrame(data, schema)`    |
| CSV/JSON/Parquet | `spark.read.csv/json/parquet(...)` |




✅ 1. From List of Tuples (like your example)

data = [("Ashu", 24), ("yogu", 28)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()


✅ 2. From List of Dictionaries

data = [{"Name": "Ashu", "Age": 24}, {"Name": "yogu", "Age": 28}]

df = spark.createDataFrame(data)
df.show()


✅ 3. From Pandas DataFrame

import pandas as pd

pdf = pd.DataFrame({"Name": ["Ashu", "yogu"], "Age": [24, 28]})
df = spark.createDataFrame(pdf)
df.show()


✅ 4. From RDD + Schema

from pyspark.sql import Row

rdd = spark.sparkContext.parallelize([Row(Name="Ashu", Age=24), Row(Name="yogu", Age=28)])
df = spark.createDataFrame(rdd)
df.show()


✅ 5. From List of Tuples + Explicit Schema

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

data = [("Ashu", 24), ("yogu", 28)]

schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)
df.show()


✅ 6. From External Files (CSV, JSON, Parquet, etc.)

# CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# JSON
df = spark.read.json("data.json")

# Parquet
df = spark.read.parquet("data.parquet")




