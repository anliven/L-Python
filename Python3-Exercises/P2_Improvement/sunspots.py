# coding=utf-8
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF

File = 'Predict.txt'
COMMENT_CHARS = '#:'

drawing = Drawing(500, 300)
data = []
with open(File, encoding="utf-8") as source:
    for line in source.readlines():
        if not line.isspace() and line[0] not in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])

predict = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

lp = LinePlot()  # 实例化LinePlot
lp.x = 50  # 设置属性
lp.y = 50
lp.height = 200
lp.width = 400
lp.data = [list(zip(times, predict)), list(zip(times, high)), list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue  # 设置折线颜色
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report.pdf', 'Sunspots')

# ### reportlab.graphics.charts.lineplots.LinePlot
# LinePlot可用于绘制折线图；
