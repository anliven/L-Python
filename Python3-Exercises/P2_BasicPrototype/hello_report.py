# coding=utf-8
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)  # 创建一个自动尺寸的Drawing对象
s = String(x=50, y=50, text='Hello, world!', textAnchor='middle')  # 创建指定属性的图形元素
d.add(s)  # 添加图形元素到Drawing对象

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')  # 以PDF格式渲染Drawing对象，并将结果保存到文件

# ### ReportLab
# HomePage: https://www.reportlab.com/
# Documentation: https://www.reportlab.com/documentation/
# 可以创建多种格式的图表文档，功能强大易于使用；
