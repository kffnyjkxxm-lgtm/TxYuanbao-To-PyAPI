import requests
import json

def test_openai_api():
    """测试OpenAI API格式"""
    
    # 基础请求
    request_data = {
        "model": "hunyuan",
        "messages": [
            {
                "role": "user",
                "content": "你好，请自我介绍一下"
            }
        ]
    }
    
    try:
        response = requests.post(
            "http://127.0.0.1:8000/v1/chat/completions",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        print("=== 基础请求 ===")
        print("状态码:", response.status_code)
        print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
        print()
    except Exception as e:
        print("请求失败:", str(e))
        print()
    
    # 多轮对话请求
    request_data = {
        "model": "hunyuan",
        "messages": [
            {
                "role": "system",
                "content": "你是一个专业的Python程序员助手"
            },
            {
                "role": "user",
                "content": "请解释Python中的装饰器"
            }
        ]
    }
    
    try:
        response = requests.post(
            "http://127.0.0.1:8000/v1/chat/completions",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        print("=== 多轮对话请求 ===")
        print("状态码:", response.status_code)
        print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
        print()
    except Exception as e:
        print("请求失败:", str(e))
        print()
    
    # 使用deepseek模型
    request_data = {
        "model": "deepseek",
        "messages": [
            {
                "role": "user",
                "content": "什么是深度学习？"
            }
        ]
    }
    
    try:
        response = requests.post(
            "http://127.0.0.1:8000/v1/chat/completions",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        print("=== DeepSeek模型请求 ===")
        print("状态码:", response.status_code)
        print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
        print()
    except Exception as e:
        print("请求失败:", str(e))
        print()
    
    # 列出可用模型
    try:
        response = requests.get(
            "http://127.0.0.1:8000/v1/models",
            headers={"Content-Type": "application/json"}
        )
        print("=== 列出可用模型 ===")
        print("状态码:", response.status_code)
        print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print("请求失败:", str(e))

if __name__ == "__main__":
    test_openai_api()
