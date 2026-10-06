--this query is to get the top item for each hour by quantity
WITH ranked_items AS (SELECT
    s.hour,
    i.item_name,
    SUM(s.quantity) AS total_quantity,
	ROW_NUMBER() OVER(
		PARTITION BY s.hour
		ORDER BY SUM(s.quantity) DESC
	) AS rank
FROM sales s
JOIN items i
    ON s.item_id = i.item_id
GROUP BY s.hour, i.item_name
ORDER BY s.hour)

SELECT
    hour,
    item_name,
    total_quantity
FROM ranked_items
WHERE rank = 1
ORDER BY hour;