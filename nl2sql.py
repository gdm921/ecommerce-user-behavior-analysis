"""自然语言转 SQL（NL2SQL）

复用 llm_client（火山方舟）的对话能力，把中文问题转成 MySQL 查询语句。
运行方式（项目根目录下）：
    python nl2sql.py          # 自测
"""
from llm_client import chat

# 把表结构告诉模型——不告诉它字段名，模型就会编造列名
TABLE_SCHEMA = """
表名: online_retail
字段:
- invoice_no: 订单号
- stock_code: 商品编码
- description: 商品描述
- quantity: 数量
- invoice_date: 订单时间，格式 2010-12-01 08:26:00
- unit_price: 单价
- customer_id: 客户ID
- country: 国家
"""

SYSTEM_PROMPT = (
    "你是数据分析助手。根据下面的表结构，把用户的中文问题转成一条 MySQL 查询语句。"
    "只输出 SQL 本身，不要任何解释，不要 markdown 代码块，不要以 ``` 开头。"
    "字段名必须来自表结构。\n"
    + TABLE_SCHEMA
)


def ask_to_sql(question: str) -> str:
    """把自然语言问题转成一条 SQL 语句。"""
    sql = chat(prompt=question, system=SYSTEM_PROMPT, temperature=0).strip()
    # 清理模型偶尔会加的 ```sql ... ``` 包裹
    if sql.startswith("```"):
        sql = sql.strip("`").strip()
        if sql.startswith("sql"):
            sql = sql[3:].strip()
    return sql


if __name__ == "__main__":
    print(ask_to_sql("哪个国家的销售额最高？"))
