Level 1: Basics & Aggregations

Calculate total revenue per product.
Count unique customers per product.  (as kont product ahe je sglyanni ghetly)
Find the most frequently purchased product.
Get average price of products sold per day.
Count total number of orders per customer.


  
🔹 Level 2: Joins & Filtering

Find customers who have never placed an order.
List products that were never purchased.
Filter services that are active and provided by specific vendors.
Join employee and department tables to show employee names with department names.
Identify orders placed in a specific quarter and calculate their total value.
  

🔹 Level 3: Window Functions

Get the first order placed by each customer.
Rank products by total revenue per quarter.
Find customers who placed multiple orders on the same day.
Calculate the running total of revenue per customer.
Assign a dense rank to customers based on total spending.


🔹 Level 4: Advanced / Telecom Use Cases

Compare service usage between two snapshots and detect decrease in usage.
Detect missing provisioning records between two systems.
Find top 3 services by data usage per access technology.
Identify customers with increasing bills across snapshots.
Find duplicate service IDs with different provisioning statuses.





ANSWER-


I can still provide you with complete answers in code form that you can copy and run in Databricks or any 
local PySpark environment.


  
✅ PySpark Problem Set — Solutions
1. Total revenue per product

sales_df.join(menu_df, "Product_id") \
    .groupBy("Product_name") \
    .agg(sum("Price").alias("total_revenue")) \
    .show()

  
2. Unique customers per product

sales_df.groupBy("Product_id") \
    .agg(countDistinct("Customer_id").alias("unique_customers")) \
    .show()

  
3. Most frequently purchased product

sales_df.groupBy("Product_id") \
    .count() \
    .orderBy("count", ascending=False) \
    .show(1)

  
4. Average price per day
(Assuming there's a date column — replace accordingly)

sales_df.groupBy("date") \
    .agg(avg("Price").alias("avg_price")) \
    .show()

 
5. Total number of orders per customer

sales_df.groupBy("Customer_id") \
    .count() \
    .withColumnRenamed("count", "total_orders") \
    .show()

 
6. Customers who never placed an order

customers_df.join(orders_df, "Customer_id", "left_anti").show()

 
7. Products that were never purchased

menu_df.join(sales_df, "Product_id", "left_anti").show()

 
8. Filter services with specific providers and statuses

rd_t_m16_uim.filter(
    (col("snapshot_id") == 336) &
    (col("RFS_ACCESS_PROV").isin("OTE", "VF")) &
    (col("CFS_STATUS") != "DISCONNECTED") &
    (col("RFS_ACCESS_TECH").isin("XDSL_RFS", "VPU_RFS", "SHDSL_RFS")) &
    (col("RFS_LOOP_NUMBER").isNotNull()) &
    (col("RFS_LOOP_NUMBER") != "0")
).show()

 
9. Join employee and department

employees_df.join(departments_df, "dept_id", "inner").show()


10. Orders in a specific quarter (e.g., 'Q1')

sales_df.filter(col("order_quarter") == "Q1") \
    .agg(sum("Price").alias("total_revenue")) \
    .show()

 
11. First order per customer (Window function)

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("Customer_id").orderBy("Order_date")

orders_df.withColumn("row_num", row_number().over(windowSpec)) \
    .filter("row_num = 1") \
    .show()

  
12. Rank products by sales per quarter

from pyspark.sql.functions import sum
from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank

joined = sales_df.join(menu_df, "Product_id") \
    .groupBy("order_quarter", "Product_name") \
    .agg(sum("Price").alias("total_sales"))

windowSpec = Window.partitionBy("order_quarter").orderBy(col("total_sales").desc())

joined.withColumn("rank", dense_rank().over(windowSpec)).show()

          
13. Customers with multiple orders on same day

sales_df.groupBy("Customer_id", "Order_date") \
    .count() \
    .filter("count > 1") \
    .show()

          
14. Running total of revenue per customer

windowSpec = Window.partitionBy("Customer_id").orderBy("Order_date") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

sales_df.withColumn("running_total", sum("Price").over(windowSpec)).show()

          
15. Dense rank of customers based on spending

from pyspark.sql.functions import sum

total_spent = sales_df.groupBy("Customer_id").agg(sum("Price").alias("total_spent"))

windowSpec = Window.orderBy(col("total_spent").desc())

total_spent.withColumn("rank", dense_rank().over(windowSpec)).show()

          
16. Compare usage between two snapshots

# Assume two DataFrames: old_df and new_df with Customer_id and usage
comparison = old_df.alias("old").join(new_df.alias("new"), "Customer_id") \
    .filter(col("new.usage") < col("old.usage")) \
    .select("Customer_id", "old.usage", "new.usage")

comparison.show()


17. Detect missing provisioning records

systemA_df.join(systemB_df, "Service_id", "left_anti").show()


18. Top 3 services by usage per tech

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("RFS_ACCESS_TECH").orderBy(col("Usage_GB").desc())

usage_df.withColumn("rank", row_number().over(windowSpec)) \
    .filter("rank <= 3") \
    .show()


19. Customers with increasing bills

windowSpec = Window.partitionBy("Customer_id").orderBy("snapshot_id")

billing_df.withColumn("prev_price", lag("price", 1).over(windowSpec)) \
    .filter(col("price") > col("prev_price")) \
    .show()


20. Duplicate service IDs with different statuses

df.groupBy("Service_id") \
    .agg(countDistinct("status").alias("status_count")) \
    .filter("status_count > 1") \
    .show()
