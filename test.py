import requests
import json
import base64

def file_to_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

print("=== 测试1: 基础OpenAI格式请求 ===")
test_data = {
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
        json=test_data,
        headers={"Content-Type": "application/json"}
    )
    print("状态码:", response.status_code)
    print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
except Exception as e:
    print("请求失败:", str(e))

print("\n=== 测试2: 使用原有格式（现在也返回OpenAI格式） ===")
test_data = {
    "sequence": "new",
    "text": "请解释什么是人工智能",
    "mode": "hunyuan"
}

try:
    response = requests.post(
        "http://127.0.0.1:8000/hunyuan",
        json=test_data,
        headers={"Content-Type": "application/json"}
    )
    print("状态码:", response.status_code)
    print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
except Exception as e:
    print("请求失败:", str(e))

print("\n=== 测试3: 列出可用模型 ===")
try:
    response = requests.get(
        "http://127.0.0.1:8000/v1/models",
        headers={"Content-Type": "application/json"}
    )
    print("状态码:", response.status_code)
    print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
except Exception as e:
    print("请求失败:", str(e))

# 取消注释以下内容测试文件上传功能
# print("\n=== 测试4: 文件上传 ===")
# test_data = {
#     "model": "hunyuan",
#     "messages": [
#         {
#             "role": "user",
#             "content": "请分析这个文件"
#         }
#     ],
#     "file1": file_to_base64("yourfile.py"),
#     "filename1": "yourfile.py"
# }
# 
# try:
#     response = requests.post(
#         "http://127.0.0.1:8000/v1/chat/completions",
#         json=test_data,
#         headers={"Content-Type": "application/json"}
#     )
#     print("状态码:", response.status_code)
#     print("响应:", json.dumps(response.json(), indent=2, ensure_ascii=False))
# except Exception as e:
#     print("请求失败:", str(e))

