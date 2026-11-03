SELECT
    month,
    COUNT(*) AS nb_orders,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM sales
WHERE amount > 0
GROUP BY month
ORDER BY month;
