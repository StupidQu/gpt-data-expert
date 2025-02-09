from config import CONFIG
import openai
import shutil
import os

client = openai.OpenAI(
    api_key='' # 填写你的 API Key
)


def extract_input(description: str) -> str:
    messages = [
        *CONFIG['EXTRACT_INPUT_MESSAGES'],
        {'role': 'user', 'content': description}
    ]
    completion = client.chat.completions.create(
        model=CONFIG['extract-input-model'],
        messages=messages,
    )
    return completion.choices[0].message.content


def generate_cyaron_code(description: str, input_format: str) -> str:
    messages = [
        *CONFIG['GENERATE_TESTDATA_MESSAGES'],
        {'role': 'user', 'content': f'题目描述如下：{description}。\n\n\n抽取的输入格式如下：{input_format}。'},
    ]
    completion = client.chat.completions.create(
        model=CONFIG['generate-model'],
        messages=messages,
    )
    messages.append(completion.choices[0].message)
    return messages, completion.choices[0].message.content


def extract_code_and_run(response: str) -> None:
    # extract code from response
    completion = client.chat.completions.create(
        model=CONFIG['extract-code-model'],
        messages=[
            *CONFIG['EXTRACT_CODE_MESSAGES'],
            {'role': 'user', 'content': response},
        ]
    )
    code = completion.choices[0].message.content
    code = code.split('```python')[1].split('```')[0]
    print(code)
    # run code
    namespace = {}
    try:
        exec(code, namespace)
    except Exception as e:
        print(f'运行脚本时出现错误，等待修复。')
        print(e)


def followup_instructions(history_messages: list[dict[str, str]], followup: str):
    completion = client.chat.completions.create(
        model=CONFIG['generate-model'],
        messages=[
            *history_messages,
            {'role': 'user', 'content': followup},
        ]
    )
    history_messages.append(followup)
    history_messages.append(completion.choices[0].message)
    return history_messages, completion.choices[0].message.content


if __name__ == '__main__':
    if not os.path.exists('./data/'):
        os.makedirs('./data/')
    else:
        delete = input('data 文件夹已存在，是否清空 (y/n):')
        if delete == 'y':
            shutil.rmtree('./data/')
            os.makedirs('./data/')
        else:
            print('请手动删除 data 文件夹后再运行。')
            exit()

    problem_description_file = input('题面文件路径，支持 markdown/html 格式：')
    std = input('标程 (std) 文件路径：')

    shutil.copyfile(std, './std.exe')

    problem_description = open(
        problem_description_file, 'r', encoding='utf-8').read()

    # Extract input format and data limitations from problem description, using gpt
    print('\n=== [STEP 1] 提取题目输入格式与数据范围 ===')
    input_format = extract_input(problem_description)
    print(input_format)
    print('=== [DONE √] 提取题目输入格式与数据范围 ===\n')

    # Generate test data using cyaron
    print('\n=== [STEP 2] 自动生成脚本 ===')
    messages, cyaron_code = generate_cyaron_code(
        problem_description, input_format)
    print(cyaron_code)
    print('=== [DONE √] 自动生成脚本 ===\n')

    # Extract code from response and run it
    print('\n=== [STEP 3] 运行脚本 ===')
    extract_code_and_run(cyaron_code)
    print('=== [DONE √] 运行脚本 ===\n')

    # Follow up instructions
    followup = input('\n === [STEP 4] 后续修改 ===\n修改指令 (为空则跳过): ')
    while followup != '':
        print('\n=== [STEP 4.1] 修改脚本 ===\n')
        messages, followup = followup_instructions(messages, followup)
        print(followup)
        print('=== [DONE √] 修改脚本 ===\n')

        print('\n=== [STEP 4.2] 运行脚本 ===\n')
        extract_code_and_run(followup)
        print('=== [DONE √] 运行脚本 ===\n')

        followup = input('修改指令 (为空则跳过): ')
    print('\n=== [DONE √] 后续修改 ===\n')
