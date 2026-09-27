# 电商用户行为数据分析项目

## 项目简介
这是一个基于 Online Retail 公开数据集的电商用户行为数据分析项目，通过 SQL 对销售数据进行多维度分析，包括基础指标统计、每日销售趋势、复购率分析、RFM 用户分层等，为电商运营提供数据支持。

## 技术栈
- 数据库：MySQL 8.0
- 数据分析：Python 3.11 + pandas
- 可视化：Streamlit（待完成）
- 版本管理：Git + GitHub

## 数据集
使用 UCI Online Retail 公开数据集，包含 2010-2011 年英国在线零售商的交易数据，共 54 万+ 条记录。
数据集地址：https://archive.ics.uci.edu/dataset/352/online+retail

## 项目结构
ecommerce-user-behavior-analysis/
├── data/               # 数据文件
│   ├── raw/            # 原始数据
│   └── processed/      # 清洗后数据
├── sql/                # SQL 分析脚本
│   ├── 01_basic_stats.sql      # 基础指标统计
│   ├── 02_daily_sales.sql      # 每日销售趋势
│   ├── 03_repurchase_rate.sql  # 复购率分析
│   ├── 04_rfm_analysis.sql     # RFM 用户分层
│   ├── 05_top_products.sql     # 热门商品 TOP10
│   └── 06_sales_by_country.sql # 各国销售分布
├── notebooks/          # Jupyter 分析（待完成）
├── dashboard/          # 可视化看板（待完成）
├── docs/               # 分析报告（待完成）
└── requirements.txt    # Python 依赖


## 核心分析内容

### 1. 基础指标统计
- 总订单数、总客户数、总销售额
- 数据清洗：剔除退货和异常值

### 2. 每日销售趋势
- 按日期统计订单数、销售额、购买客户数
- 观察销售趋势和周期性

### 3. 复购率分析
- 统计只买1次的客户数 vs 买2次以上的客户数
- 计算客户复购率

### 4. RFM 用户分层
- R（Recency）：最近一次购买距今天数
- F（Frequency）：购买频率
- M（Monetary）：消费金额
- 将客户分为：重要价值客户、重要保持客户、新客户、流失客户、一般客户

### 5. 热门商品分析
- 统计销量和销售额最高的 TOP10 商品

### 6. 各国销售分布
- 按国家统计销售额、订单数、客户数

## 如何运行
1. 克隆仓库：`git clone git@github.com:gdm921/ecommerce-user-behavior-analysis.git`
2. 导入数据到 MySQL
3. 执行 sql/ 目录下的 SQL 文件

## 后续规划
- [ ] 使用 pandas 进行数据可视化
- [ ] 使用 Streamlit 搭建交互式看板
- [ ] 撰写完整的分析报告
- [ ] 使用 Spark 重写数据处理逻辑，向大数据开发方向扩展
