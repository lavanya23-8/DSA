# Write your MySQL query statement below
select
   stock_name,
   SUM(
    CASE
        WHEN operation = 'sell' THEN price
         ELSE -price
    END     
   )AS capital_gain_loss
From Stocks
GROUP BY stock_name;   