-- 项目：复购率分析
-- 功能：统计总客户数、只买1次的客户数、买2次以上的客户数、复购率
-- 日期：2026-09-23

USE ecommerce;

SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN order_count = 1 THEN 1 ELSE 0 END) AS one_time_customers,
    SUM(CASE WHEN order_count >= 2 THEN 1 ELSE 0 END) AS repeat_customers,
    ROUND(SUM(CASE WHEN order_count >= 2 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS repurchase_rate
FROM (
    SELECT customer_id, COUNT(DISTINCT invoice_no) AS order_count
    FROM online_retail
    WHERE quantity > 0 AND unit_price > 0
    GROUP BY customer_id
) AS customer_orders;
