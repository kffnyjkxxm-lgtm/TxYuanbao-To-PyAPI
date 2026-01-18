# TxYuanbao-To-PyAPI  
<h2>基于Python Selenium的Flask API，用于使用Python脚本操控腾讯AI元宝网页的输入上传发送等操作并检测元宝AI的输出将其返回为json，以创建一个腾讯元宝驱动的AI API接口</h2>  
<h2>原理就是拿你的电脑挂着腾讯元宝网页当api用</h2>

<h3>演示效果如下</h3>

![屏幕截图 2025-06-01 003013](https://github.com/user-attachments/assets/19176373-dd67-47b4-8d0d-e70b8d23bc1c)

py环境3.0以上即可，已提供源代码，需要修改(自行看代码注释)或打包等请自行操作  

---
<h2>部署api方法(直接使用源代码,windows,使用edge浏览器)：</h2>  
<h3>

- 请先pip安装python库：pip install selenium webdriver-manager flask requests apscheduler
- git仓库或将代码文件aiapi.py，setbrowser.py复制至同一目录下后，打开cmd窗口，cd至目录
- 输入python aiapi.py，等待元宝页面打开后自行使用账号登录(有cookie记录功能,登录一次后面就不需要登啦)
- 运行成功

</h3>
<h3>以上步骤不要太频繁，之后保持窗口运行</h3>  

---
<h2>访问api方式：</h2>
<h3>
   
   > 兼容OpenAI API格式，使用标准接口即可调用腾讯元宝AI
</h3>

<h3>基础对话</h3>
端点: `POST /v1/chat/completions`

接收json格式:
```json
{
  "model": "hunyuan",
  "messages": [
    {
      "role": "user",
      "content": "你好，请自我介绍一下"
    }
  ]
}
```

支持的模型: `hunyuan`, `deepseek`

<h3>多模态对话（图片上传）</h3>
接收json格式（OpenAI标准格式）:
```json
{
  "model": "hunyuan",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "这张图片是什么？"},
        {"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}
      ]
    }
  ]
}
```

<h3>多轮对话</h3>
```json
{
  "model": "hunyuan",
  "messages": [
    {
      "role": "system",
      "content": "你是一个专业的Python编程助手"
    },
    {
      "role": "user",
      "content": "什么是装饰器？"
    },
    {
      "role": "assistant",
      "content": "装饰器是一种..."
    },
    {
      "role": "user",
      "content": "能给个例子吗？"
    }
  ]
}
```

<h3>响应格式</h3>
```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "hunyuan",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "AI响应内容"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 200,
    "total_tokens": 300
  }
}
```

<h3>列出可用模型</h3>
端点: `GET /v1/models`

<h3>兼容原有格式</h3>
端点: `POST /hunyuan` （返回OpenAI格式响应）

<h3>
   
   > 注意事项：已成功实现多线程，setbrowser.py中的最大标签页数量就是线程的数量，且部分设置可在setbrowser.py中进行设置，如线程数量，端口，使用浏览器等等
</h3>

## 项目维护

若您正在使用我的项目对我的项目有新的需求或发现bug请向于本项目内报告，一般3-7天内会给出答复，后期可能会视作品小星星der数量增加更多功能！由于此项目时效性，我会每隔2-4月进行运行测试是否可正常运行

<h3>作者的话：我tm服了为什么市赛不用ai，省赛直接ai漫天飞？？？这私人题目还必须得用ai搞，老子还没钱充ai的api，勾吧信息比赛(赛名我就不说了)，密码的我直接做个api挂nat机上，花钱是不可能的！</h3>
