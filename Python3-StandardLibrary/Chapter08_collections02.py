#! python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import json


def create_tree():
    return defaultdict(create_tree)


root = create_tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(type(root))
print(json.dumps(root, indent=4))

# 使用collections模块的defaultdict构造树形数据结构
