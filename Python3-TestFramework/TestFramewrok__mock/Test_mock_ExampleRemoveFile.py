# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from ExampleRemoveFile import rm


class RmTestCase(unittest.TestCase):

    @patch('ExampleRemoveFile.os')
    def test_rm(self, mock_os):
        rm("any path")  # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
