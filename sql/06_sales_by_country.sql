--按国家分组，统计每个国家的销售额、订单数、客户数。

SELECT 
    country AS 国家,
    COUNT(DISTINCT invoice_no) AS 订单数,
    COUNT(DISTINCT customer_id) AS 客户数,
    ROUND(SUM(quantity * unit_price), 2) AS 销售额
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY country
ORDER BY 销售额 DESC;
