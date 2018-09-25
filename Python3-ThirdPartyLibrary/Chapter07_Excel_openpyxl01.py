# coding=utf-8
from openpyxl import Workbook
import datetime
import os

wb = Workbook()
ws = wb.active  # grab the active worksheet

ws['A1'] = 42  # Data can be assigned directly to cells
ws.append([1, 2, 3])  # Rows can also be appended
ws['A2'] = datetime.datetime.now()  # Python types will automatically be converted

wb.save("sample.xlsx")  # Save the file
wb.close()

os.remove("sample.xlsx")

# ### openpyxl
# - openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
# - Homepage: http://www.python-excel.org/
# - Documentation: https://openpyxl.readthedocs.org
