# 对拍器 Compare
将对拍器与您的数据生成器结合使用，您可以方便地检测您的程序的正确性。

1. 对拍输出文件
```python
# 默认比较器为NOIP风格，忽略最后空行和行尾空格
Compare.output("1.out", "2.out", std="std.out") 
# 以std.out为标准，对比1.out和2.out的正确性

std_io = IO()
std_io.output_writeln(1, 2, 3) # 往std_io的output里写入一些东西
Compare.output("1.out", "2.out", std=std_io) 
# 以std_io这个IO对象中的output为标准，对拍1.out和2.out，
```

2. 对拍程序
```python
input_io = IO()
input_io.input_write("1111\n")

Compare.program("a.exe", input=input_io, std_program="std.exe") 
# 以input_io这个IO对象中的input为stdin输入。
# std.exe的输出为标准输出，以此为标准对拍a.exe的输出。

Compare.program("a.exe", "b.exe", input=input_io, std_program="std.exe") 
# 和上面的方法类似，但是你可以以std.exe为标准对拍多个程序输出。

Compare.program("a.exe", "b.exe", "c.exe", input="data.in", std="std.out") 
# 当然input也可以简单地是文件，并以std.out这个输出文件的内容来对a.exe, b.exe, c.exe对拍。
# 这里std也可以是IO对象。

while True:
    input_io = IO()
    input_io.input_writeln(randint(1,100))
    Compare.program("a.exe", "b.exe", input=input_io, std_program="std.exe") 
# 不断地生成测试数据（这里是1到100的随机数），然后放到a.exe，b.exe中，分别以std.exe为标准进行对拍比较
# CYaRon 现在使用多线程比较器，原 stop_on_incorrect 参数现已 deprecated 且无实际作用。
```
对于对拍程序的附加提示：CYaRon将每一个参数视为shell命令执行，也就是说在Linux下有必要写成`./a`, `./b`等。

3. 使用其他比较器

CYaRon内置`NOIPStyle`和`FullText`两种比较器，默认为`NOIPStyle`，更换比较器的方法如下：
```python
Compare.program("a.exe", input=input_io, std_program="std.exe", grader="FullText")
```

您也可以自己撰写比较器，请参考如下的代码示例。
```python
from cyaron import *
from cyaron.graders import CYaRonGraders

@CYaRonGraders.grader("MyGrader")
def my_grader(content, std):
    if is_correct: # 请自行改为判断是否正确的逻辑
        return True, None
    else:
        return False, "Answer incorrect!"

Compare.program("a.exe", input=input_io, std_program="std.exe", grader="MyGrader")
```
