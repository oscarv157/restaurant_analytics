--This is to rank each hour by sale
SELECT s.hour ,SUM(s.sales) AS total_sale, SUM(s.quantity) AS total_quantity
FROM sales s
GROUP BY s.hour
ORDER BY total_sale DESC;