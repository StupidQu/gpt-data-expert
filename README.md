# gpt-data-expert

通过题目描述与 std 全自动生成测试数据。

https://github.com/user-attachments/assets/e491720a-9191-48d2-ade4-ab41ab3834cb

需要 Python 版本 >=3.8，在 Python 3.13.2 上测试成功。

先 clone 本项目：`git clone https://github.com/StupidQu/gpt-data-expert.git`

修改 `main.py`，填写你的 OpenAI Key：

```py
client = openai.OpenAI(
    base_url='https://api.openai.com/v1',
    api_key='sk-......'
)
```

修改 `config.py`，选择你需要使用的模型（在 `config.py` 的最下面）：

```py
CONFIG = {
    'EXTRACT_INPUT_MESSAGES': EXTRACT_INPUT_MESSAGES,
    'GENERATE_TESTDATA_MESSAGES': GENERATE_TESTDATA_MESSAGES,
    'EXTRACT_CODE_MESSAGES': EXTRACT_CODE_MESSAGES,
    'extract-input-model': 'gpt-4o-mini',  # 用于从题面中抽取输入格式与数据要求的模型
    'generate-model': 'gpt-4o',  # 用于创建生成数据的脚本的模型，需要高智能或编程模型
    'extract-code-model': 'gpt-4o-mini',  # 用于从生成的回答中抽取代码
}
```

安装必要的依赖：`pip install openai cyaron`，之后**通过 `python main.py` 运行**。


