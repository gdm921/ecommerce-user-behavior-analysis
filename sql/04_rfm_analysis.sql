--指标	含义	怎么算
--R（Recency）	客户最近一次买东西距今天数	今天 - 客户最后一次购买日期--
--F（Frequency）	客户一共买了多少次	统计订单数
--M（Monetary）	客户一共花了多少钱	统计总消费金额

USE ecommerce;

SELECT 
    customer_id,
    DATEDIFF('2011-12-09', MAX(invoice_date)) AS recency,  -- R：距今天数
    COUNT(DISTINCT invoice_no) AS frequency,               -- F：购买次数
    ROUND(SUM(quantity * unit_price), 2) AS monetary          -- M：总消费金额
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY customer_id
ORDER BY monetary DESC;

