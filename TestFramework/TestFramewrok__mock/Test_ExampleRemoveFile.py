# -*- coding: utf-8 -*-
from ExampleRemoveFile import rm
import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):
    TmpFilePath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.TmpFilePath, "w") as f:
            f.write("Delete me!")

    def test_rm(self):  # remove the file
        rm(self.TmpFilePath)  # test that it was actually removed
        self.assertFalse(os.path.isfile(self.TmpFilePath), "Failed to remove the file.")


if __name__ == '__main__':
    unittest.main()
