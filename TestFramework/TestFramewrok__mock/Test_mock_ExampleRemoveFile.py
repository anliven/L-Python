# -*- coding: utf-8 -*-
__author__ = 'Anliven'

### 使用mock重构测试用例

from ExampleRemoveFile import rm
import mock
import unittest


class RmTestCase(unittest.TestCase):

    @mock.patch('ExampleRemoveFile.os')
    def test_rm(self, mock_os):
        rm("any path")        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

if __name__ == '__main__':
    unittest.main()