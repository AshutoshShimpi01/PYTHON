
Question 1 : Find the customers whose total purchase value is more than double their refund value 


WITH CustomerSummary AS (

SELECT c_id, SUM(purchase_value) AS total_purchase,
       SUM(refund_value) AS total_refund
FROM transactions
GROUP BY c_id
)
SELECT c_id
FROM CustomerSummary
WHERE total_purchase > 2 * total_refund;



  
Question 2 : Identify the cities with more than 3 purchases 


SELECT city, COUNT(*) AS purchase_count
FROM transactions -- 
WHERE transaction_type = 'Purchase' -- Filtering the base data for purchases
GROUP BY city
HAVING COUNT(*) > 3;



   
Question 3 : Find the second highest transaction for first city 

WITH RankedTransactions AS
(
SELECT *,
DENSE_RANK() OVER (PARTITION BY city ORDER BY t_amount DESC) AS rank_num
FROM transactions
)
SELECT city, t_id, c_id, t_amount
FROM RankedTransactions
WHERE rank_num = 2 AND city = (SELECT MIN(city) FROM transactions);
                           
------
SAME USING SUBQUERY
------

SELECT  t.transaction_amount
FROM transactions t
WHERE t.city = (SELECT MIN(city) FROM transactions) 
ORDER BY t.transaction_amount DESC
OFFSET 1 
LIMIT 1; 






---------
PYSPARK
---------

from pyspark.sql import SparkSession 
   spark = SparkSession.builder.getOrCreate()
   df = spark.read.csv("s3_path + orders.csv",headers=True,inferschema=True)

     
# Question 1 : Find the top three customers by total order value 
ANS :- 100%
     
df.groupBy('cust_id').agg(sum('price').alias('total_paid')).orderBy(col('total_paid').desc()).limit(3).show()



# Question 2 : Identify customers whose total order value is higher than the city average

from pyspark.sql.functions import sum, avg, col

# 1. Calculate the average order value per city
avg_df = df.groupBy("city").agg(avg("o_amt").alias("avg_city_v"))
# 2. Join the main df with the city average
df_avg_city = df.join(avg_df, on="city")
# 3. Calculate total spending per customer
final_df = df_avg_city.groupBy("c_id", "city", "avg_city_v").agg(sum("o_amt").alias("total_order_value"))
final_df.filter(col("total_order_value") > col("avg_city_v")).show()
    
