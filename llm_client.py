"""DeepSeek OpenAI 兼容接口客户端

接入要点：
- base_url : https://api.deepseek.com
- API Key  : https://platform.deepseek.com/api_keys
- 模型     : deepseek-chat（默认，便宜够用）

使用方式：
    from llm_client import chat
    reply = chat("帮我总结一下今天的数据")
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 读取项目根目录 .env 中的 DEEPSEEK_API_KEY / DEEPSEEK_MODEL

BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-chat"


def get_client() -> OpenAI:
    """创建 DeepSeek 客户端，未配置 Key 时给出明确提示。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "未设置 DEEPSEEK_API_KEY。请在项目根目录 .env 文件中填入你的 DeepSeek API Key，"
            "获取地址：https://platform.deepseek.com/api_keys"
        )
    return OpenAI(base_url=BASE_URL, api_key=api_key)


def chat(
    prompt: str,
    system: str = "你是电商数据分析助手，回答专业、简洁、有条理。",
    model: str | None = None,
    temperature: float = 0.7,
    max_tokens: int | None = None,
) -> str:
    """单轮对话，返回模型回复文本。

    参数:
        prompt: 用户输入
        system: 系统提示词
        model: 模型 ID，默认取 .env 中 DEEPSEEK_MODEL
        temperature: 采样温度
        max_tokens: 最大输出 token 数
    """
    client = get_client()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    kwargs = {
        "model": model or os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL),
        "messages": messages,
        "temperature": temperature,
    }
    if max_tokens:
        kwargs["max_tokens"] = max_tokens

    resp = client.chat.completions.create(**kwargs)
    return resp.choices[0].message.content


if __name__ == "__main__":
    # 命令行自测：python llm_client.py
    print(chat("用一句话介绍你自己"))
