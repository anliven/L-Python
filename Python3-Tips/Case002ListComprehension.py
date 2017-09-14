# -*- coding: utf-8 -*-

listOne = [1, 2, 3, 4, 5]
listTwo = [2 * i for i in listOne if i > 2]
print('listOne:', listOne)
print('listTwo:', listTwo)

# ### 列表推导（List Comprehension）
# - 用于从一份现有的列表中得到一份新列表，原始列表依旧保持不变；
# - 适用于根据旧表建立新表的场景，有效减少代码数量;
