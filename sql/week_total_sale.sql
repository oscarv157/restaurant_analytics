--This list the sales made for each week
SELECT w.week_start, w.week_end, SUM(s.sales) AS total_sale, SUM(s.quantity) AS total_quantity
FROM sales s
JOIN weeks w
	ON s.week_id = w.week_id
GROUP BY w.week_id
ORDER BY w.week_id