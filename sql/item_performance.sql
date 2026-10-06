--
WITH top_item AS (
    SELECT
        s.item_id
    FROM sales s
    GROUP BY s.item_id
    ORDER BY SUM(s.sales) DESC
    LIMIT 1
)

SELECT
    w.week_start,
    w.week_end,
    i.item_name,
    SUM(s.sales) AS total_sales,
    SUM(s.quantity) AS total_quantity
FROM sales s
JOIN weeks w
    ON s.week_id = w.week_id
JOIN items i
    ON s.item_id = i.item_id
JOIN top_item t
    ON s.item_id = t.item_id
GROUP BY
    w.week_start,
    w.week_end,
    i.item_name
ORDER BY
    w.week_start;