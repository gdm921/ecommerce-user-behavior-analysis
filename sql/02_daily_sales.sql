-- 项目：每日销售趋势分析
-- 功能：基础指标统计（日期（哪天的数据）、订单数（当天）、销售额（当天）、购买客户数（当天））
-- 日期：2026-09-22


USE ecommerce;

SELECT 
    DATE(invoice_date) AS '日期',
    COUNT(DISTINCT invoice_no) AS '订单数',
    ROUND(SUM(quantity * unit_price), 2) AS '销售额',
    COUNT(DISTINCT customer_id) AS '购买客户数'
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY DATE(invoice_date)
ORDER BY 'se日期';
