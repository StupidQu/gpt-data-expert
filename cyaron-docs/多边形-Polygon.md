# 多边形 Polygon
使用Polygon库您可以输入、生成多边形，并对其进行一些简单的操作。
```python
p = Polygon([(0,0), (0,4), (4,4), (4,0)]) # 以这四个点生成四边形，注意点需要按照连线顺序
p.perimeter() # 周长
p.area() # 面积
io.input_writeln(p)

# 您也可以使用以下的模板生成随机的多边形
p = Polygon.convex_hull(n) # 生成一个N个点的凸包
p = Polygon.simple_polygon(n) # 生成一个N个点的简单多边型
```
有关于Polygon库的更多高级用法，请参见源代码。
