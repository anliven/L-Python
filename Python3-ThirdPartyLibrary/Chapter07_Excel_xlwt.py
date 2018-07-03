# coding=utf-8
import xlwt


def set_style(name, height, bold=False):  # 设置样式
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel():
    wb = xlwt.Workbook()  # 创建工作簿
    work_sheet = wb.add_sheet('Test', cell_overwrite_ok=True)  # 创建sheet

    row0 = ["Name", "Age", "Position", "Hobby", "DateTime"]
    column0 = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    for i in range(0, len(row0)):  # 写入第一行
        work_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    for i in range(0, len(column0)):  # 写入第一列
        work_sheet.write(i + 1, 0, column0[i], set_style('Times New Roman', 220, True))

    work_sheet.write(1, 1, '29')  # 写入单元格内容
    work_sheet.write_merge(1, 2, 3, 3, 'Football')  # 合并单元格，第4列的第2和第3行
    work_sheet.write_merge(3, 3, 1, 3, 'Unknown')  # 合并单元格，第3行的第2到第4列
    work_sheet.write_merge(4, 5, 3, 3, 'Basketball', set_style('Times New Roman', 220, True))

    work_sheet2 = wb.add_sheet('Test2', cell_overwrite_ok=True)  # 通过add_sheet()创建多个sheet
    work_sheet2.write(1, 1, '2012/12/12')

    wb.save('Chapter07_Excel_xlwt_Test.xls')  # 保存文件


if __name__ == '__main__':
    write_excel()

# ### xlwt
# This package is for writing data and formatting information to older Excel files (ie: .xls)；
# PyPI：https://pypi.org/project/xlwt/
# Homepage：http://www.python-excel.org/
#
# ### 写入合并单元格的内容
# write_merge(x, x+m, y, y+n, string, style)
# - “x, x+m, y, y+n”：行、跨行个数、列、跨列个数，都以0开始计数；
# - string: 写入的单元格内容；
# - style：单元格样式；
