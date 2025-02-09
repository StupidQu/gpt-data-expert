# 图 Graph
Graph库可以用来生成各种各样的树、图、链等结构。

这个库中本身已经配备了各种常用的图的模板，不过我们先来看看手动建立一个图的方法。

```python
graph = Graph(10) # 建立一个10个节点的无向图
graph = Graph(10, directed=True) # 建立一个10个节点的有向图
# 这两个图的节点编号范围都为1到10

graph.add_edge(1, 5) # 建立一条从1到5，权值为1的边，若是无向图，还会建立从5到1的边
graph.add_edge(1, 6, weight=3) # 建立一条从1到6，权值为3的边，若是无向图，还会建立从6到1的边

graph.edges # 一个邻接表数组，每一维度i保存的是i点出发的所有边，以Edge对象存储
for edge in graph.iterate_edges(): # 遍历所有边，其中edge内保存的也是Edge对象
    edge.start # 获取这条边的起点
    edge.end # 获取这条边的终点
    edge.weight # 获取这条边的边权
    io.input_writeln(edge) # 输出这条边，以u v w的形式

io.input_writeln(graph) # 输出这个图，以每条边u v w一行的格式
io.input_writeln(graph.to_str(shuffle=True)) # 打乱边的顺序并输出这个图
io.input_writeln(graph.to_str(output=my_func)) # 使用my_func函数替代默认的输出函数，请查看源代码以理解使用方法
io.input_writeln(graph.to_str(output=Edge.unweighted_edge)) # 输出无权图，以每条边u v一行的格式
```
不过在大多数情况下您不需要手动建图，我们为您准备了大量模板，用法如下：
```python
graph = Graph.graph(n, m) # 生成一个n点，m边的无向图，边权均为1
graph = Graph.graph(n, m, directed=True, weight_limit=(5, 300)) # 生成一个n点，m边的有向图，边权范围是5到300
graph = Graph.graph(n, m, weight_limit=20) # 生成一个n点，m边的无向图，边权范围是1到20
graph = Graph.graph(n, m, weight_gen=my_func) # 生成一个n点，m边的无向图，使用自定义随机函数my_func的返回值作为边权
graph = Graph.graph(n, m, self_loop=False, repeated_edges=False) # 生成一个n点，m边的无向图，禁止重边和自环
# 以上的directed, weight_limit, weight_gen参数，对如下的所有函数都有效。

chain = Graph.chain(n) # 生成一条n个节点的链，是Graph.tree(n, 1, 0)的别名
flower = Graph.flower(n) # 生成一朵n个节点的菊花图，是Graph.tree(n, 0, 1)的别名
tree = Graph.tree(n) # 生成一棵n个节点的随机树
tree = Graph.tree(n, 0.4, 0.35) # 生成一棵n个节点的树，其中40%的节点呈现链状，35%的节点呈现菊花图状，剩余25%的节点随机加入
binary_tree = Graph.binary_tree(n) # 生成一棵n个节点的随机二叉树
binary_tree = Graph.binary_tree(n, 0.4, 0.35) # 生成一棵n个节点的二叉树，其中节点有40%的概率是左儿子，35%的概率是右儿子，25%的概率被随机选择
graph = Graph.hack_spfa(n) # 生成一个n点，1.5*n(下取整)边的图，具有卡SPFA的特点
graph = Graph.hack_spfa(n, extra_edge=m) # 生成一个n点，1.5*n+m(下取整)边的图，具有卡SPFA的特点
# 下列方法生成的图保证连通
# 支持 self_loop, repeated_edges, weight_limit, weight_gen 参数，但不支持 directed，DAG 的 self_loop 默认为 False
graph = Graph.DAG(n, m) # 生成一个 n 点，m 边的有向无环图
graph = Graph.DAG(n, m, loop=True) # 生成一个 n 点，m 边的有向有环图
graph = Graph.UDAG(n, m) # 生成一个 n 点，m 边的无向联通图
```