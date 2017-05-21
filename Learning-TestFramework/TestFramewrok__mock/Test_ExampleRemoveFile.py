# -*- coding: utf-8 -*-
__author__ = 'Anliven'

### 传统的unittest测试用例 : 一个临时文件被创建然后被删除

from ExampleRemoveFile import rm
import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):

    TmpFilePath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.TmpFilePath, "wb") as f:
            f.write("Delete me!")

    def test_rm(self):  # remove the file
        rm(self.TmpFilePath)        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.TmpFilePath), "Failed to remove the file.")

if __name__ == '__main__':
    unittest.main()

# 把上面的内容保存到Test_ExampleRemoveFile.py中，命令行进入相应目录，执行“python Test_ExampleRemoveFile.py -v” 就可以运行测试了。