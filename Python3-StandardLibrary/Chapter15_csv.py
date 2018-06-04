import csv
import os

csv_file = "test.csv"

with open(csv_file, "wt", newline="") as f:  # 参数newline设置一行文本的结束字符
    w = csv.writer(f, dialect="excel", delimiter="#")  # 以excel方式打开，分隔符为“#”
    w.writerow(("index", "char", "num"))  # 插入一行数据
    for i in range(3):
        w.writerow((i + 1, chr(ord('a') + i), i * i))

with open(csv_file, "rt") as f:
    r = csv.reader(f, delimiter='#')
    # print(list(r))
    for row in r:
        print(row)
        print(row[1])

os.remove(csv_file)

# ### 标准库csv模块
# - CSV File Reading and Writing
# - https://docs.python.org/3/library/csv.html
# - 源码文件: Python安装目录\Lib\csv.py；
