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

--用窗口函数做 RFM 分层
SELECT 
    customer_id,
    recency,
    frequency,
    monetary,
    NTILE(4) OVER (ORDER BY recency ASC) AS r_score,
    NTILE(4) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(4) OVER (ORDER BY monetary DESC) AS m_score
FROM (
    -- 子查询要写完整
    SELECT 
        customer_id,
        DATEDIFF('2011-12-09', MAX(invoice_date)) AS recency,
        COUNT(DISTINCT invoice_no) AS frequency,
        ROUND(SUM(quantity * unit_price), 2) AS monetary
    FROM online_retail
    WHERE quantity > 0 AND unit_price > 0
    GROUP BY customer_id
) AS rfm_base;

--客户分层
SELECT 
    customer_id,
    recency,
    frequency,
    monetary,
    r_score,
    f_score,
    m_score,
    CASE 
        WHEN r_score = 4 AND f_score = 4 AND m_score = 4 THEN '重要价值客户'
        WHEN r_score = 1 AND f_score = 4 AND m_score = 4 THEN '重要保持客户'
        WHEN r_score = 4 AND f_score = 1 AND m_score = 1 THEN '新客户'
        WHEN r_score = 1 AND f_score = 1 AND m_score = 1 THEN '流失客户'
        ELSE '一般客户'
    END AS customer_type
FROM (
    -- 第二层：打分（用窗口函数）
    SELECT 
        customer_id,
        recency,
        frequency,
        monetary,
        NTILE(4) OVER (ORDER BY recency ASC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency DESC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary DESC) AS m_score
    FROM (
        -- 第一层：计算每个客户的RFM基础值
        SELECT 
            customer_id,
            DATEDIFF('2011-12-09', MAX(invoice_date)) AS recency,
            COUNT(DISTINCT invoice_no) AS frequency,
            ROUND(SUM(quantity * unit_price), 2) AS monetary
        FROM online_retail
        WHERE quantity > 0 AND unit_price > 0
        GROUP BY customer_id
    ) AS rfm_base
) AS rfm_scored;


