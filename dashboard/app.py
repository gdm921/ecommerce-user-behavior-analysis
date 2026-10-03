import sys
import os

# 把项目根目录加入模块搜索路径，才能 import 到根目录的 llm_client / nl2sql
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import pymysql
from nl2sql import ask_to_sql

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

# ===== AI 数据分析师（自然语言查数据）=====
st.header("AI 数据分析师")
question = st.text_input("用中文提问，比如：哪个国家的销售额最高？", "")
if st.button("AI 查询"):
    if not question.strip():
        st.warning("请输入问题")
    else:
        with st.spinner("AI 正在生成 SQL..."):
            try:
                sql = ask_to_sql(question)
            except Exception as e:
                st.error(f"AI 调用失败：{e}")
                st.stop()
        st.code(sql, language="sql")
        try:
            result = pd.read_sql(sql, conn)
        except Exception as e:
            st.error(f"SQL 执行失败：{e}，换个问法试试")
            st.stop()
        st.dataframe(result)
        if len(result.columns) >= 2:
            st.bar_chart(result.set_index(result.columns[0])[result.columns[1]])
