# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

tree = ET.parse('Chapter11_XML02.xml')  # 读取文件
root = tree.getroot()  # 获取根元素
print(root.tag, root.attrib)  # 根元素的标签和属性
print(root[1][2].text)  # 通过索引访问特定的元素

for child in root:  # 迭代子节点的标签和属性
    print(child.tag, child.attrib)

for neighbor in root.iter('neighbor'):  # 递归遍历指定元素的标签、属性和值
    print(neighbor.tag, neighbor.text, neighbor.attrib)

for country in root.findall('country'):  # 找到符合的直接子元素对象
    rank = country.find('rank').text  # 找到符合的第一个子元素，并访问内容
    name = country.get('name')  # 访问属性
    print(name, rank)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)  # 改变文本
    rank.set('updated', 'yes')  # 修改属性

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)  # 删除元素

new_xml = 'Chapter11_XML02-new.xml'
tree.write(new_xml)  # 写入更改并构建XML文档
os.remove(new_xml)

# 通过XPath读取XML内容
xml = r"""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""

root2 = ET.fromstring(xml)  # 读取字符串
print(root2.findall("."))  # 找到根元素
print(root2.findall("./country/neighbor"))  # 找到根元素下指定的元素
print(root2.findall(".//neighbor[2]"))  # 第二个子元素下的所有neighbor元素
print(root2.findall(".//year/..[@name='Singapore']"))  # 找到名为Singapore的元素，并且包含一个year子元素
print(root2.findall(".//*[@name='Singapore']/year"))  # 找到Singapore元素下的year元素
print(root2.findall(".//*[@name='Singapore']/year")[0].text)  # 访问Singapore元素下的year元素的文本内容

# 生成XML内容
r = ET.Element("root")  # 创建根元素
a = ET.SubElement(r, 'sub1', attrib={'name': 'AAA', 'num': "111"}, con="test")  # 创建子元素并添加属性
b = ET.SubElement(r, "sub2")  # 创建子元素
b.attrib = {"name": "BBB"}  # 添加属性
c = ET.SubElement(r, "sub3")  # 创建子元素
c.text = "test3"  # 添加文本
ET.dump(r)  # 在标准输出显示元素的树结构（建议只用于调试）
tree2 = ET.ElementTree(r)  # 创建ElementTree对象
new_xml2 = 'Chapter13_StandradLibrary11_XML02-new2.xml'
tree2.write(new_xml2)  # 构建XML文档
os.remove(new_xml2)

# ### xml package
# - XML Processing Modules
# - https://docs.python.org/3/library/xml.html
#
# ### 标准库xml.etree.ElementTree模块
# - The ElementTree XML API(实现用于解析和创建XML数据的简单有效的API)
# - https://docs.python.org/3/library/xml.etree.elementtree.html
