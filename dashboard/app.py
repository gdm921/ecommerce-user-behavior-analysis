import streamlit as st
import pandas as pd
import pymysql

st.title("电商数据分析看板")

# 连接数据库（直接用pymysql）
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='hzhf0421',  
    database='ecommerce',
    charset='utf8mb4'
)

# 查询数据
sql = "SELECT * FROM online_retail WHERE quantity > 0 AND unit_price > 0 LIMIT 100"
df = pd.read_sql(sql, conn)

st.write("数据预览：")
st.dataframe(df)
# ===== 核心指标卡片 =====
st.header("核心指标")

# 查询基础指标
basic_sql = """
SELECT 
    COUNT(DISTINCT invoice_no) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(quantity * unit_price), 2) AS total_sales
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
"""
basic_df = pd.read_sql(basic_sql, conn)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("总订单数", f"{basic_df['total_orders'][0]:,}")
with col2:
    st.metric("总客户数", f"{basic_df['total_customers'][0]:,}")
with col3:
    st.metric("总销售额", f"£{basic_df['total_sales'][0]:,.2f}")

# ===== 每日销售趋势 =====
st.header("每日销售趋势")
daily_sql = """
SELECT 
    DATE(invoice_date) AS sale_date,
    ROUND(SUM(quantity * unit_price), 2) AS daily_sales
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY DATE(invoice_date)
ORDER BY sale_date
"""
daily_df = pd.read_sql(daily_sql, conn)
st.line_chart(daily_df.set_index('sale_date')['daily_sales'])

# ===== 各国销售分布 =====
st.header("各国销售分布")
country_sql = """
SELECT 
    country,
    ROUND(SUM(quantity * unit_price), 2) AS sales
FROM online_retail
WHERE quantity > 0 AND unit_price > 0
GROUP BY country
ORDER BY sales DESC
LIMIT 10
"""
country_df = pd.read_sql(country_sql, conn)
st.bar_chart(country_df.set_index('country')['sales'])
