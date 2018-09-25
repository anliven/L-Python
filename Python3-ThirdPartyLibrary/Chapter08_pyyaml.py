# -*- coding: utf-8 -*-
import yaml
import os

current_real_path = os.path.split(os.path.realpath(__file__))[0]
file_path = os.path.join(current_real_path, 'Chapter08_pyyaml_config.yaml')

with open(file_path, 'r', encoding='utf-8') as f:
    content = yaml.load(f.read())
    print(type(content))
    # print(content)
    print(content['version'])  # 通过索引
    print(content['handlers']['file']['level'])
    print(content.get('root'))  # 通过get()方法
    print(content.get('root').get('handlers'))

data = {'Test': {'isTest': True, 't1': 12.3, 't2': ['bbb', 222], 't3': None}}

with open(file_path, 'a', encoding='utf-8') as f:
    yaml.dump(data, f)

# ### pyyaml
# - PyYAML is a YAML parser and emitter for Python.
# - HomePage: http://pyyaml.org/wiki/PyYAML
# - Documentation: https://pyyaml.org/wiki/PyYAMLDocumentation
#
# ### YAML（Yet Another Markup Language）
# YAML实质上是一种通用的数据串行化格式，适用于编写配置文件，非常简洁和强大，比JSON格式更方便；
# 基本语法规则：
# - 1.大小写敏感
# - 2.使用缩进表示层级关系，并且只能使用空格缩进
# - 4.缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
# - 5.使用“#”表示注释，从这个字符一直到行尾的内容都会被忽略
# 支持的数据格式：
# - 1.对象：键值对的集合（又称为映射mapping、哈希hashes、字典dictionary）
# - 2.数组：序列sequence、列表list
# - 3.纯量：单个不可再分的值，例如布尔值、整数、浮点数、Null、时间日期等
