# -*- coding: utf-8 -*-
__author__ = 'Anliven'

### 被测试代码

import os


def rm(filename):  # 从文件系统中删除文件
    # if os.path.isfile(filename):
        os.remove(filename)