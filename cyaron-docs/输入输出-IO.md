# 输入输出 IO

IO库可以方便的帮您建立一组测试数据。构造函数的调用方法有以下几种：
```python
IO("test1.in", "test1.out") # test1.in, test1.out
IO(file_prefix="test") # test.in, test.out
IO(file_prefix="test", data_id=3) # test3.in, test3.out
IO(file_prefix="test", data_id=6, input_suffix=".input", output_suffix=".answer") # test6.input, test6.answer
IO("test2.in") # test2.in, .out文件生成为临时文件
IO(file_prefix="test", data_id=5, disable_output=True) # test5.in, 不建立.out
IO() # .in, .out文件均生成为临时文件，一般配合对拍器使用
```
以上方法可以帮您创建一组测试数据的文件。其中使用`file_prefix`和`data_id`配合`for`循环可以较为方便地批量生成多个数据点。

IO库的方法主要有以下几种：
```python
io = IO("test1.in", "test1.out") # 先新建一组数据
io.input_write(1, 2, 3) # 写入1 2 3到输入文件
io.input_writeln(4, 5, 6) # 写入4 5 6到输入文件并换行
io.output_write(1, 2, 3) # 写入1 2 3到输出文件
io.output_writeln(4, 5, 6) # 写入4 5 6到输出文件并换行
io.input_write([1, 2, 3]) # 写入1 2 3到输入文件
io.output_write(1, 2, [1, 2, 3], [4]) # 写入1 2 1 2 3 4到输出文件
io.input_write(1, 2, 3, separator=',') # 写入1,2,3,到输入文件，目前版本尾部会多一个逗号，之后可能修改行为
io.output_gen("~/Documents/std") # 执行shell命令或二进制文件，把输入文件的内容通过stdin送入，获得stdout的内容生成输出
io.output_gen("C:\\Users\\Aqours\\std.exe") # 当然Windows也可以
```