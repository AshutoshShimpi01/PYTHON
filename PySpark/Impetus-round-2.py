
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
