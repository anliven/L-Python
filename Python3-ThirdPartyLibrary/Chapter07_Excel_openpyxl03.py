# coding=utf-8
import openpyxl

wb = openpyxl.load_workbook(filename="Chapter07_Excel_openpyxl_Test.xlsx")

ws = wb['Sheet-One']
print("# Current active Worksheet: ", ws, "# Title: ", ws.title)
print("Size:{} MaxMinRow:{} MaxMinColumn:{}".format(ws.dimensions,
                                                    (ws.max_row, ws.min_row),
                                                    (ws.max_column, ws.min_column)))

for row in ws.rows:  # 按行遍历获取单元格
    print("# rows:", row)
    for cell in list(row):  # 逐个打印单元格信息
        print("# rows value:{} RowColumn:{} Coordinate:{}".format(cell.value, (cell.row, cell.column), cell.coordinate))

for row in ws.values:  # 按行遍历获取单元格
    print("# rows value:", *row)

for row in ws.iter_rows(min_row=2, max_row=4, min_col=2, max_col=4):
    print("# ws.iter_rows: ", list(row))

print(wb['Sheet-Two']['A1'], wb['Sheet-Two'].cell(row=1, column=2))  # 获取Cell对象的两种方式

wb.close()

# ### Worksheet对象
# 通过Workbook对象可以获取表格的属性，得到单元格中的数据，修改表格中的内容；
# 常见的Worksheet属性和方法（大部分都是返回Cell对象，一个Cell对象代表一个单元格）
#   - title：表格的标题
#   - dimensions：表格的大小（含有数据的表格的左上角坐标和右下角坐标）
#   - max_row：表格的最大行
#   - min_row：表格的最小行
#   - max_column：表格的最大列
#   - min_column：表格的最小列
#   - rows：按行获取单元格(Cell对象)
#   - columns：按列获取单元格(Cell对象)
#   - values：按行获取表格的内容(数据)
#   - freeze_panes：冻结窗格，主要用于在表格较大时冻结顶部的行或左边的行
#   - iter_rows：按行获取所有单元格，内置属性有(min_row,max_row,min_col,max_col)
#   - iter_columns：按列获取所有的单元格
#   - append：在表格末尾添加数据
#   - merged_cells：合并多个单元格
#   - unmerged_cells：移除合并的单元格
#
# ### Cell对象
# 一个Cell对象代表一个单元格；
# 获取Cell对象：
#   - 使用Excel坐标的方式
#   - 使用Worksheet的cell方法
# 常见的Cell属性和方法
#   - row：单元格所在的行
#   - column：单元格坐在的列
#   - value：单元格的值
#   - coordinate：单元格的坐标
