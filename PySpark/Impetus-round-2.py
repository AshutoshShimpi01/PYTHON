
Question 1 : Find the customers whose total purchase value is more than double their refund value 


WITH CustomerSummary AS (
    -- Step 1: Aggregate total purchase value and total refund value for each customer
    SELECT
        c_id,
        SUM(purchase_value) AS total_purchase,
        SUM(refund_value) AS total_refund
    FROM
        transactions
    GROUP BY
        c_id
)
-- Step 2: Filter for customers where total purchase is more than double the refund
SELECT
    c_id
FROM
    CustomerSummary
WHERE
    total_purchase > 2 * total_refund;



  
Question 2 : Identify the cities with more than 3 purchases 


SELECT
    city,
    COUNT(*) AS purchase_count
FROM
    transactions -- CORRECTED: Should be the table containing transaction details
WHERE
    transaction_type = 'Purchase' -- Filtering the base data for purchases
GROUP BY
    city
HAVING
    COUNT(*) > 3; -- Filtering the aggregated groups (cities);



   
Question 3 : Find the second highest transaction for first city 

WITH RankedTransactions AS (
    -- Step 1: Rank ALL transactions, partitioned by city
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY city ORDER BY t_amount DESC) AS rank_num
    FROM
        transactions
)
-- Step 2: Select the row where the rank is 2 AND the city matches the 'first' city
SELECT
    city,
    t_id,
    c_id,
    t_amount
FROM
    RankedTransactions
WHERE
    -- Filter 1: Isolate the second highest transaction
    rank_num = 2
    AND
    -- Filter 2: Isolate the transaction belonging to the 'first' city (alphabetically)
    city = (SELECT MIN(city) FROM transactions);


------
SUBQUERY
------

SELECT
    t.transaction_amount
FROM
    transactions t
WHERE
    t.city = (SELECT MIN(city) FROM transactions) -- Isolate the transactions of the first city
ORDER BY
    t.transaction_amount DESC
OFFSET 1 -- Skip the 1st highest transaction
LIMIT 1;  -- Take the next one (the 2nd highest)
