import pandas as pd
from sqlalchemy import create_engine

# 1. 连接数据库
engine = create_engine('mysql+pymysql://root:hzhf0421@localhost:3306/ecommerce?charset=utf8mb4')

# 2. 读取Excel文件
df = pd.read_excel('data/raw/Online Retail.xlsx')

# 3. 重命名列名，和数据库表对应
df.columns = ['invoice_no', 'stock_code', 'description', 'quantity', 
              'invoice_date', 'unit_price', 'customer_id', 'country']

# 4. 导入到MySQL表
df.to_sql('online_retail', engine, if_exists='append', index=False)

print("数据导入完成！")
