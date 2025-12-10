Here’s a **simple, clear example** of how to **repartition** data in PySpark.

## ✔️ Basic Example: `repartition()`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RepartitionExample").getOrCreate()

# Create a simple DataFrame
data = [("Alice", 34), ("Bob", 25), ("Charlie", 30), ("David", 29)]
df = spark.createDataFrame(data, ["name", "age"])

print("Initial partitions:", df.rdd.getNumPartitions())

# Repartition to 4 partitions (shuffle occurs)
df_repartitioned = df.repartition(4)

print("Partitions after repartition:", df_repartitioned.rdd.getNumPartitions())
```

### ✔️ What `repartition()` does

* Increases or decreases number of partitions.
* **Always triggers a full shuffle** of the data.
* Good for distributing data more evenly before large operations (e.g., joins).

---

## ✔️ Example with column-based repartition

```python
df_by_age = df.repartition(3, "age")
print(df_by_age.rdd.getNumPartitions())
```

This shuffles data so that rows with the same `age` tend to end up in the same partition.

---

## ✔️ `coalesce()` (bonus comparison)

If you just want to **reduce** partitions *without a full shuffle*, use `coalesce()`:

```python
df_small = df.coalesce(1)
print(df_small.rdd.getNumPartitions())
```

---

If you want, I can show:

* repartition vs coalesce performance comparison,
* how to inspect partition content,
* how to repartition RDDs instead of DataFrames.
