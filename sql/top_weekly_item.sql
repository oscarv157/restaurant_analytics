--This is displaying the top 5 sold items each week
WITH ranked_items AS (SELECT
	w.week_start,
	w.week_end,
    i.item_name,
    SUM(s.quantity) AS total_quantity,
	ROW_NUMBER() OVER(
		PARTITION BY w.week_id
		ORDER BY SUM(s.quantity) DESC
	) AS rank
FROM sales s
JOIN items i
    ON s.item_id = i.item_id
JOIN weeks w
	ON s.week_id = w.week_id
GROUP BY i.item_name, w.week_id
ORDER BY w.week_id)

SELECT
	week_start,
	week_end,
    item_name,
    total_quantity
FROM ranked_items
WHERE rank IN (1,2,3,4,5)
ORDER BY week_start;