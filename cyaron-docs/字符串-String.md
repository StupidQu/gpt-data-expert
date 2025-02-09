# 字符串 String
String库可以帮您生成各种随机字符串、单词、句子、段落等。

使用方法如下：
```python
str = String.random(5) # 生成一个5个字母的单词，从小写字母中随机选择
str = String.random((10, 20), charset="abcd1234") # 生成一个10到20个字母之间的单词，从abcd1234共8个字符中随机选择
str = String.random(10, charset="#######...") # 生成一个10个字母的只有'#'和'.'组成的字符串，'#'的可能性是70%，'.'可能30%。
str = String.random(None, charset=["foo", "bar"]) # 从foo、bar两个单词中随机选择一个返回
# charset参数对于以下所有指令也有效。

str = String.random_sentence(5) # 生成一个5个单词的句子，以空格分割，第一个单词首字母自动大写，结尾有句号或感叹号，每个单词3到8个字母长
str = String.random_sentence((10, 20), word_separators=",;", sentence_terminators=None, first_letter_uppercase=False, word_length_range=(2, 10), charset="abcdefg") # 生成一个10到20个单词的句子，以逗号或分号随机分割，第一个单词首字母不大写，结尾没有任何符号，每个单词2到10字母长，从abcdefg共7个字符中随机选择
# 以上所有参数，对于以下所有指令也有效

str = String.random_paragraph((3, 10)) # 生成一个3到10个句子的段落，句子之间以句号或感叹号分割，小句之间以逗号或分号分割，句子和小句结束后均接有一个空格，句子开头首字母大写而小句开头首字母不大写。生成句子的可能性为30%而小句的可能性为70%。
str = String.random_paragraph(6, sentence_joiners="|", sentence_separators=",", sentence_terminators=".?", termination_percentage=0.1) # 生成一个6个句子的段落，句子之间以句号或问号号分割，小句之间以逗号分割，句子和小句结束后均接有一个"|"号，句子开头首字母大写而小句开头首字母不大写。生成句子的可能性为10%而小句的可能性为90%。

# 注意：如果您需要以两个空格分割单词，应该使用如下写法：
str = String.random_sentence(5, word_separators=["  "]) # 以两个空格分割单词
# 而不是：
str = String.random_sentence(5, word_separators="  ") # 这会导致从两个空格中随机选择一个，也就是只有一个空格
```