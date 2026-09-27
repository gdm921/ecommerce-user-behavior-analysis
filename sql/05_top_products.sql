--思路：按商品分组，统计销量和销售额，取前 10。

USE ecommerce;

SELECT 
    description AS 商品名称,
    SUM(quantity) AS 销售件数,
    ROUND(SUM(quantity * unit_price), 2) AS 销售额
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY description
ORDER BY 销售件数 DESC
LIMIT 10;
