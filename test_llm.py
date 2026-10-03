"""火山方舟接入自测脚本

运行方式（项目根目录下）：
    python test_llm.py
"""
from llm_client import chat

if __name__ == "__main__":
    reply = chat("你好，用一句话介绍你自己，再告诉我你是谁家的模型。")
    print("模型回复：")
    print(reply)
