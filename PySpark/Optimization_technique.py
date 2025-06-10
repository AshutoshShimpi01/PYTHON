Spark Optimization Techniques


🔹 1. Use DataFrames and Spark SQL instead of RDDs
DataFrames are optimized by Catalyst Optimizer and Tungsten engine, making them faster and more memory-efficient than RDDs.


🔹 2. Persist/Cache DataFrames When Reused

df.cache()       # Stores in memory
df.persist()     # Can store in memory + disk
Avoids recomputation across stages.
  

🔹 3. Broadcast Small DataFrames
 
from pyspark.sql.functions import broadcast

df.join(broadcast(small_df), "id")
Avoids costly shuffles by sending small data to all executors.


🔹 4. Avoid Wide Transformations Where Possible
Prefer narrow transformations like map, filter instead of wide ones like groupByKey, repartition.
                                                                                   

🔹 5. Use coalesce() Instead of repartition() When Reducing Partitions
 
df.coalesce(4)   # Faster, avoids full shuffle


🔹 6. Filter Early ("Push Down" Filters)
Apply .filter() as early as possible to reduce data processed in the next stages.
  

🔹 7. Use select() Instead of *
 
df.select("id", "name")   # Avoid df.select("*")
Only bring necessary columns for better memory and performance.
  

🔹 8. Avoid Collecting Large Datasets to Driver
 
df.show()     # Good
df.collect()  # Dangerous if large

  
🔹 9. Tune Spark Configurations
Examples:

spark.sql.shuffle.partitions = 100  # default is 200
spark.executor.memory = 4g
spark.executor.cores = 4


🔹 10. Use Partitioning and Bucketing for Large Tables
Helps with faster reads and joins:


df.write.partitionBy("country").parquet("path/")


🔹 11. Avoid UDFs Unless Necessary
Prefer Spark SQL functions (from pyspark.sql.functions) over UDFs because UDFs are slower and not optimized.


🔹 12. Enable Adaptive Query Execution (AQE)
Dynamically optimizes joins and partitions at runtime.

spark.conf.set("spark.sql.adaptive.enabled", "true")

  
🔹 13. Use Columnar Formats Like Parquet/ORC
They're compressed and support predicate pushdown.


🔹 14. Use explain() and queryExecution to Analyze Execution Plan
 
df.explain(True)
df.queryExecution.debug.codegen()  # For advanced tuning


🔹 15. Skew Join Optimization
Use salting or broadcast joins to handle skewed data.
