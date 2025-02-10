import os


PROBLEM_C1003 = r"""## 题目背景

命题人：心灵震荡

众所周知，数学对于 OI 是相当重要的。狼人嚎想出一些数学题考考你。

## 题目描述

狼人嚎有一些数学题，它的内容是这样的：给定一个区间 $[l, r]$，问该区间内所有 $k$ 的倍数的和是多少？

狼人嚎共有 $t$ 道这样的题。

## 输入格式

第一行一个整数 $t$，表示共 $t$ 次询问。

第 $2\sim t + 1$ 行，每行 $3$ 个整数 $l, r, k$，意义见【题目描述】。

## 输出格式

对于每组询问，输出答案。

## 输入输出样例

```input1
3
1 10 2
3 11 4
1 1 4
```

```output1
30
12
0
```

## 提示说明

### 样例解释

对于第一组询问，$1\sim 10$ 中有 $2, 4, 6, 8, 10$ 是 $2$ 的倍数，它们的和为 $2+4+6+8+10=30$。

对于第二组询问，$3\sim 11$ 中有 $4, 8$ 是 $4$ 的倍数，它们的和为 $4+8=12$。

对于第三组询问，$1\sim 1$ 中不存在 $4$ 的倍数，故输出 $0$。

### 数据范围

共 $20$ 组测试数据，通过一组数据可以获得 $5$ 分。

| 测试点编号 | $1\le t \le$ | $1\le l \le r \le$ | $1\le k \le$ |
| :----------: | :----------: | :----------: | :----------: |
| $1$ | $1$ | $10^3$ | $1$ |
| $2 \sim 9$ | $10^3$ | $10^5$ | $10^5$ |
| $10$ | $10^5$ | $10^9$ | $2$ |
| $11 \sim 20$ | $10^5$ | $10^9$ | $10^9$"""
PROBLEM_C1003_INPUT = r"""共 20 组数据，对于每组数据：

第一行一个整数 $t$，表示共 $t$ 次询问。

第 $2\sim t + 1$ 行，每行 $3$ 个整数 $l, r, k$，代表一个区间 [l, r] 和一个整数 k。

对于各组数据，数据范围如下：

| 测试点编号 | $1\le t \le$ | $1\le l \le r \le$ | $1\le k \le$ |
| :----------: | :----------: | :----------: | :----------: |
| $1$ | $1$ | $10^3$ | $1$ |
| $2 \sim 9$ | $10^3$ | $10^5$ | $10^5$ |
| $10$ | $10^5$ | $10^9$ | $2$ |
| $11 \sim 20$ | $10^5$ | $10^9$ | $10^9$ |"""
PROBLEM_C1003_CYARON = r"""好的，我现在要使用 CYaRon 库生成题目的数据，题目的数据分成了四个部分：第 1 组，第 2~9 组，第 10 组，第 11~20 组。

我应该根据不同的组别，生成不同的数据。我可以用 CYaRon 提供的 randint 函数生成一个随机数。在生成结束后，我应该调用用户的标准程序获得正确的输出。

我注意到，如果 k 过大，这个题目将变的非常简单，所以为了测试数据的强度，我需要让 k 不那么大。

对于这个题目，代码如下：

```python
from cyaron import *

def generate_one_query(io, maxr, maxk):
    r = randint(maxr // 2, maxr)
    l = randint(1, maxr)
    k = randint(1, maxk)
    io.input_writeln(l, r, k)

def generate_one_data(io, t, maxr, maxk):
    io.input_writeln(t)
    for i in range(t):
        generate_one_data(io, maxr, maxk)
    io.output_gen('std.exe') # 调用用户的标准程序，获得输出

# 对于第 1 组数据
io = IO(file_prefix='./data/data', data_id=1)
generate_one_data(io, 1, 10**3, 1)

# 对于第 2~9 组数据
for i in range(2, 10):
    io = IO(file_prefix='./data/data', data_id=i)
    generate_one_data(io, 10**3, 10**5, 10**5 // 4) # 为了数据强度，将 k 改为 10**5 / 4 

# 对于第 10 组数据
io = IO(file_prefix='./data/data', data_id=10)
generate_one_data(io, 10**5, 10**9, 2)  

# 对于第 11~20 组数据
for i in range(2, 10):
    io = IO(file_prefix='./data/data', data_id=i)
    generate_one_data(io, 10**5, 10**9, 10**8) # 为了数据强度，将 k 改为 10**8
```

这个代码应该可以生成用户想要的数据。
"""
PROBLEM_C1003_CYARON_CODE = r"""```python
from cyaron import *

def generate_one_query(io, maxr, maxk):
    r = randint(maxr // 2, maxr)
    l = randint(1, maxr)
    k = randint(1, maxk)
    io.input_writeln(l, r, k)

def generate_one_data(io, t, maxr, maxk):
    io.input_writeln(t)
    for i in range(t):
        generate_one_data(io, maxr, maxk)
    io.output_gen('std.exe') # 调用用户的标准程序，获得输出

# 对于第 1 组数据
io = IO(file_prefix='./data/data', data_id=1)
generate_one_data(io, 1, 10**3, 1)

# 对于第 2~9 组数据
for i in range(2, 10):
    io = IO(file_prefix='./data/data', data_id=i)
    generate_one_data(io, 10**3, 10**5, 10**5 // 4) # 为了数据强度，将 k 改为 10**5 / 4 

# 对于第 10 组数据
io = IO(file_prefix='./data/data', data_id=10)
generate_one_data(io, 10**5, 10**9, 2)  

# 对于第 11~20 组数据
for i in range(2, 10):
    io = IO(file_prefix='./data/data', data_id=i)
    generate_one_data(io, 10**5, 10**9, 10**8) # 为了数据强度，将 k 改为 10**8
```"""

PROBLEM_CF555E = r"""<div>
 <p>
  Andrewid the Android is a galaxy-known detective. Now he is preparing a defense against a possible attack by hackers on a major computer network.
 </p>
 <p>
  In this network are
  <span class="tex-span">
   <i>
    n
   </i>
  </span>
  vertices, some pairs of vertices are connected by
  <span class="tex-span">
   <i>
    m
   </i>
  </span>
  undirected channels. It is planned to transfer
  <span class="tex-span">
   <i>
    q
   </i>
  </span>
  important messages via this network, the
  <span class="tex-span">
   <i>
    i
   </i>
  </span>
  -th of which must be sent from vertex
  <span class="tex-span">
   <i>
    s
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  to vertex
  <span class="tex-span">
   <i>
    d
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  via one or more channels, perhaps through some intermediate vertices.
 </p>
 <p>
  To protect against attacks a special algorithm was developed. Unfortunately it can be applied only to the network containing directed channels. Therefore, as new channels can't be created, it was decided for each of the existing undirected channels to enable them to transmit data only in one of the two directions.
 </p>
 <p>
  Your task is to determine whether it is possible so to choose the direction for each channel so that each of the
  <span class="tex-span">
   <i>
    q
   </i>
  </span>
  messages could be successfully transmitted.
 </p>
</div>


<div class="">
 <h2 class="">
  Input
 </h2>
 <p>
  The first line contains three integers
  <span class="tex-span">
   <i>
    n
   </i>
  </span>
  ,
  <span class="tex-span">
   <i>
    m
   </i>
  </span>
  and
  <span class="tex-span">
   <i>
    q
   </i>
  </span>
  (
  <span class="tex-span">
   1 ≤
   <i>
    n
   </i>
   ,
   <i>
    m
   </i>
   ,
   <i>
    q
   </i>
   ≤ 2·10
   <sup class="upper-index">
    5
   </sup>
  </span>
  ) — the number of nodes, channels and important messages.
 </p>
 <p>
  Next
  <span class="tex-span">
   <i>
    m
   </i>
  </span>
  lines contain two integers each,
  <span class="tex-span">
   <i>
    v
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  and
  <span class="tex-span">
   <i>
    u
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  (
  <span class="tex-span">
   1 ≤
   <i>
    v
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ,
   <i>
    u
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ≤
   <i>
    n
   </i>
  </span>
  ,
  <span class="tex-span">
   <i>
    v
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ≠
   <i>
    u
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  ), that means that between nodes
  <span class="tex-span">
   <i>
    v
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  and
  <span class="tex-span">
   <i>
    u
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  is a channel. Between a pair of nodes can exist more than one channel.
 </p>
 <p>
  Next
  <span class="tex-span">
   <i>
    q
   </i>
  </span>
  lines contain two integers
  <span class="tex-span">
   <i>
    s
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  and
  <span class="tex-span">
   <i>
    d
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  (
  <span class="tex-span">
   1 ≤
   <i>
    s
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ,
   <i>
    d
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ≤
   <i>
    n
   </i>
  </span>
  ,
  <span class="tex-span">
   <i>
    s
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
   ≠
   <i>
    d
   </i>
   <sub class="lower-index">
    <i>
     i
    </i>
   </sub>
  </span>
  ) — the numbers of the nodes of the source and destination of the corresponding message.
 </p>
 <p>
  It is not guaranteed that in it initially possible to transmit all the messages.
 </p>
</div>


<div class="">
 <h2 class="">
  Output
 </h2>
 <p>
  If a solution exists, print on a single line "
  <span class="tex-font-style-tt">
   Yes
  </span>
  " (without the quotes). Otherwise, print "
  <span class="tex-font-style-tt">
   No
  </span>
  " (without the quotes).
 </p>
</div>



```input1
4 4 2
1 2
1 3
2 3
3 4
1 3
4 2
```


```output1
Yes
```


```input2
3 2 2
1 2
3 2
1 3
2 1
```


```output2
No
```


```input3
3 3 2
1 2
1 2
3 2
1 3
2 1
```


```output3
Yes
```

<div class="">
 <h2 class="">
  Note
 </h2>
 <p>
  In the first sample test you can assign directions, for example, as follows:
  <span class="tex-span">
   1 → 2
  </span>
  ,
  <span class="tex-span">
   1 → 3
  </span>
  ,
  <span class="tex-span">
   3 → 2
  </span>
  ,
  <span class="tex-span">
   4 → 3
  </span>
  . Then the path for for the first message will be
  <span class="tex-span">
   1 → 3
  </span>
  , and for the second one —
  <span class="tex-span">
   4 → 3 → 2
  </span>
  .
 </p>
 <p>
  In the third sample test you can assign directions, for example, as follows:
  <span class="tex-span">
   1 → 2
  </span>
  ,
  <span class="tex-span">
   2 → 1
  </span>
  ,
  <span class="tex-span">
   2 → 3
  </span>
  . Then the path for the first message will be
  <span class="tex-span">
   1 → 2 → 3
  </span>
  , and for the second one —
  <span class="tex-span">
   2 → 1
  </span>
  .
 </p>
</div>"""
PROBLEM_CF555E_INPUT = r"""第一行包含三个整数 \( n \)、\( m \) 和 \( q \) （\( 1 \leq n, m, q \leq 2 \times 10^5 \)）——节点数、通道数和重要信息数。

接下来的 \( m \) 行每行包含两个整数 \( v_i \) 和 \( u_i \) （\( 1 \leq v_i, u_i \leq n \)，\( v_i \neq u_i \)），表示节点 \( v_i \) 和节点 \( u_i \) 之间有一条通道。同一对节点之间可以有多条通道。

接下来的 \( q \) 行每行包含两个整数 \( s_i \) 和 \( d_i \) （\( 1 \leq s_i, d_i \leq n \)，\( s_i \neq d_i \)）——对应信息的源节点和目标节点。

初始时并不保证所有信息都能被传输。"""
PROBLEM_CF555E_CYARON = r"""好的，我现在要使用 CYaRon 库生成题目的数据。题目的测试数据只有一个部分。首先我需要生成 n, m, q 代表节点数，边数和查询数。

接下来我需要生成一个无向图 G ，用户需要给这个无向图定向，满足我给出的 q 个查询，从 u 都能到达 v。我可以使用 CYaRon 提供的 Graph 来生成一个图。接下来随机生成查询。

用户没有指定生成数据的组数，所以我默认生成 10 组数据。在生成结束后，我应该调用用户的标准程序获得正确的输出。

对于这个输入，代码如下：
```python
from cyaron import *

for i in range(1, 11): # 生成 10 组数据
    io = IO(file_prefix='./data/data', data_id=i)
    n = randint(10**5, 2*10**5)
    m = randint(n, 2*10**5)
    q = randint(1, n)

    G = Graph.graph(n, m)

    io.input_writeln(n, m, q)
    io.input_writeln(G.to_str(output=Edge.unweighted_edge)) # 以 u v 的格式输出

    for _ in range(q):
        u = randint(1, n)
        v = u
        while u == v:
            v = randint(1, n)
        io.input_writeln(u, v)

    io.output_gen('std.exe')
```
"""
PROBLEM_CF555E_CYARON_CODE = r"""```python
from cyaron import *

for i in range(1, 11): # 生成 10 组数据
    io = IO(file_prefix='./data/data', data_id=i)
    n = randint(10**5, 2*10**5)
    m = randint(n, 2*10**5)
    q = randint(1, n)

    G = Graph.graph(n, m)

    io.input_writeln(n, m, q)
    io.input_writeln(G.to_str(output=Edge.unweighted_edge)) # 以 u v 的格式输出

    for _ in range(q):
        u = randint(1, n)
        v = u
        while u == v:
            v = randint(1, n)
        io.input_writeln(u, v)

    io.output_gen('std.exe')
```"""

EXTRACT_INPUT_MESSAGES = [
    {'role': 'system', 'content': 'I have the following competitive programming problem, I want to generate test data for this problem. Please extract the input format and data limitations from the problem description.'},
    {'role': 'user', 'content': PROBLEM_C1003},
    {'role': 'assistant', 'content': PROBLEM_C1003_INPUT},
    {'role': 'user', 'content': PROBLEM_CF555E},
    {'role': 'assistant', 'content': PROBLEM_CF555E_INPUT},
]

CYARON_DOCS = "以下是数据生成库 CYARON 的文档：\n"
# iterate over ./cyaron-docs/ and read all files to CYARON DOCS
for doc in os.listdir('./cyaron-docs/'):
    with open('./cyaron-docs/' + doc, 'r', encoding='utf-8') as f:
        CYARON_DOCS += f'# {doc} \n{f.read()}\n'

GENERATE_TESTDATA_SYSTEM_PROMPT = f"""
现在我想要为一个题目生成数据，请你帮我写一段 Python 代码，调用 CYaRon 库提供的数据生成工具，生成对应的测试数据。

{CYARON_DOCS}

在输入数据生成完毕后，你需要调用用户的标准程序，在本地的 std.exe 中，你可以通过 io.output_gen('std.exe') 来调用它。请注意，我使用
windows 运行这个脚本，所以务必保证使用 io.output_gen('std.exe') 而不是 io.output_gen('./std.exe') 等。

请务必把生成的测试数据存在 ./data/ 文件夹下，否则会拒绝你的请求。你可以通过更改 IO 的 file_prefix='./data/xxx' 来实现这一点。
"""
GENERATE_TESTDATA_MESSAGES = [
    {'role': 'system', 'content': GENERATE_TESTDATA_SYSTEM_PROMPT},
    {'role': 'user', 'content': f'题目描述如下：{PROBLEM_C1003}。\n\n\n抽取的输入格式如下：{PROBLEM_C1003_INPUT}。'},
    {'role': 'assistant', 'content': PROBLEM_C1003_CYARON},
    {'role': 'user', 'content': f'题目描述如下：{PROBLEM_CF555E}。\n\n\n抽取的输入格式如下：{PROBLEM_CF555E_INPUT}。'},
    {'role': 'assistant', 'content': PROBLEM_CF555E_CYARON},
]

EXTRACT_CODE_MESSAGES = [
    {'role': 'system', 'content': '我有以下的文本，请你从文本中抽取可以执行的 Python 代码，只需要给出 Python 代码，以 ```python 开头，以 ``` 结束。'},
    {'role': 'user', 'content': PROBLEM_C1003_CYARON},
    {'role': 'assistant', 'content': PROBLEM_C1003_CYARON_CODE},
    {'role': 'user', 'content': PROBLEM_CF555E_CYARON},
    {'role': 'assistant', 'content': PROBLEM_CF555E_CYARON_CODE},
]

CONFIG = {
    'EXTRACT_INPUT_MESSAGES': EXTRACT_INPUT_MESSAGES,
    'GENERATE_TESTDATA_MESSAGES': GENERATE_TESTDATA_MESSAGES,
    'EXTRACT_CODE_MESSAGES': EXTRACT_CODE_MESSAGES,
    'extract-input-model': 'gpt-4o-mini',
    'generate-model': 'gpt-4o-mini',
    'extract-code-model': 'gpt-4o-mini',
}
