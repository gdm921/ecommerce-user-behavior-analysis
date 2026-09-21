-- 项目：电商用户行为数据分析
-- 功能：基础指标统计（总记录数、订单数、客户数、销售额）
-- 日期：2026-09-21

USE ecommerce;

SELECT 
    COUNT(*) AS total_records,
    COUNT(DISTINCT invoice_no) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(quantity * unit_price), 2) AS total_sales
FROM online_retail
WHERE quantity > 0 AND unit_price > 0;
