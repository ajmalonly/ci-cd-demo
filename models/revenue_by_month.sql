SELECT
    month,
    COUNT(*) AS nb_orders,
    ROUND(SUM(amount), 2) AS total_amount
FROM sales
WHERE amount > 0
GROUP BY month
ORDER BY month;
