# coding=utf-8
import xlrd
from datetime import date

file = 'Chapter07_Excel_xlrd_Test.xls'
wb = xlrd.open_workbook(filename=file, formatting_info=True)  # formatting_info参数设置为False，用以获取合并单元格内容等
print("# All the worksheet names: ", wb.sheet_names())

s_1 = wb.sheet_by_index(1)  # 通过索引（从0开始计数）获取表格
print("# Sheet1-Name: %s   Rows*Cols: %s*%s" % (s_1.name, s_1.nrows, s_1.ncols))  # 获取sheet名称、行数和列数
print("Row num 1：", s_1.row_values(1))  # 获取指定行内容
print("Col num 2：", s_1.col_values(2))  # 获取指定列内容
print("Cell:", s_1.cell(1, 0).value,
      s_1.cell_value(1, 0).encode('utf-8'),
      s_1.row(1)[0].value.encode('utf-8'))  # 获取单元格内容的方式

s_2 = wb.sheet_by_name('测试')  # 通过名字获取表格
print("# Sheet2-Name: %s   Rows*Cols: %s*%s" % (s_2.name, s_2.nrows, s_2.ncols))

s_3 = wb.sheet_by_name('Test3')
print("# Sheet3-Name: %s   Rows*Cols: %s*%s" % (s_3.name, s_3.nrows, s_3.ncols))
if s_3.cell(3, 3).ctype == 3:  # “cell(3, 3).ctype”等同于“cell_type(3, 3)”
    dt_value = xlrd.xldate_as_tuple(s_3.cell_value(3, 3), wb.datemode)  # 使用时间格式处理，获取日期格式单元格的内容
    print("Date time:", dt_value, date(*dt_value[:3]), date(*dt_value[:3]).strftime('%Y/%m/%d'))
print("Merge cell:", s_3.merged_cells)  # 获取合并单元格
print(s_3.cell_value(3, 0))  # 获取合并单元格的内容，使用merge_cells返回row和col的低位索引即可
for (row, row_range, col, col_range) in s_3.merged_cells:
    print(s_3.cell_value(row, col))

# ### xlrd
# This package is for reading data and formatting information from older Excel files (ie: .xls)；
# PyPI：https://pypi.org/project/xlrd/
# Homepage：http://www.python-excel.org/
#
# ### 读取日期格式单元格的内容
# python读取excel单元格内容，返回值有5种类型(ctype)：0(empty)、1(string)、2(number)、3(date)、4(boolean)、5(error)；
# 如果ctype为3，需要使用xlrd的xldate_as_tuple来处理为date格式；
#
# ### 读取合并单元格的内容
# merged_cells()：获取合并单元格，返回结果的形式为“(row,row_range,col,col_range)”；
# 例如(7, 8, 2, 6)的含义是第7行的第2到5列为合并单元格；
# 只能通过合并单元格第一个cell的行列索引来获取合并单元格的内容，否则会得到空值；
