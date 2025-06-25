Awesome! You're on the right track — learning PySpark through real-world problems is the best way to master it.

Let’s go step by step. I’ll give you a variety of PySpark problems, each with increasing complexity and related to data engineering, ETL, or telecom-like use cases. You can try solving them, and I’ll help if you get stuck.

🔹 Level 1: Basics & Aggregations
Problem 1: Total Revenue per Product
Tables:

sales_df → columns: Product_id, Customer_id, Price

menu_df → columns: Product_id, Product_name

✅ Task: Join sales_df with menu_df and calculate total revenue per Product_name.

Problem 2: Count of Unique Customers per Product
Same data as above.

✅ Task: For each product, find out how many unique customers purchased it.

🔹 Level 2: Joins & Filtering
Problem 3: Customers with No Orders
Tables:

customers_df: Customer_id, Name

orders_df: Order_id, Customer_id

✅ Task: Find customers who never placed an order.

Problem 4: Services Not Disconnected (Telecom style)
Table: rd_t_m16_uim
Columns: snapshot_id, RFS_ACCESS_PROV, CFS_STATUS, RFS_ACCESS_TECH, RFS_LOOP_NUMBER

✅ Task: Filter rows where:

snapshot_id = 336

RFS_ACCESS_PROV in ('OTE', 'VF')

CFS_STATUS ≠ 'DISCONNECTED'

RFS_ACCESS_TECH in ('XDSL_RFS', 'VPU_RFS', 'SHDSL_RFS')

RFS_LOOP_NUMBER is not null or 0

Then, check if those rows are present in another table like wcrm_rl.

🔹 Level 3: Window Functions
Problem 5: Find First Order per Customer
Table: orders → Customer_id, Order_date, Order_id

✅ Task: For each customer, get their first order using window function.

Problem 6: Rank Products by Sales Per Quarter
Tables:

sales_df: Product_id, Price, order_quarter

menu_df: Product_id, Product_name

✅ Task: Join tables and rank products per quarter based on total revenue.

🔹 Level 4: Advanced Use Cases
Problem 7: Compare Snapshots to Detect Revenue Leakage
Table: billing_data
Columns: Customer_id, snapshot_id, price

✅ Task: For each Customer_id, compare price between two snapshot_ids and find customers whose price decreased in the new snapshot.

Problem 8: Top N Services by Volume (per Technology)
Table: usage_data
Columns: Service_id, RFS_ACCESS_TECH, Usage_GB

✅ Task: For each RFS_ACCESS_TECH, find top 3 services with highest Usage_GB.

