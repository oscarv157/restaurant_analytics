--This is ranking each item by quantities sold, top 10
SELECT i.item_name, SUM(s.sales) AS total_sale, SUM(s.quantity) AS total_quantity
FROM sales s
JOIN items i
	ON s.item_id = i.item_id
GROUP BY i.item_name
ORDER BY total_quantity DESC
LIMIT 10;