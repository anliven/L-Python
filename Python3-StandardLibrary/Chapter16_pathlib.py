# -*- coding: utf-8 -*-
import sys
import pathlib


class DirTree():
    """生成目录树
    @ pathname: 目标目录
    @ filename: 要保存成文件的名称
    """

    def __init__(self, pathname='.', filename='Chapter16_dir_tree.txt'):
        super(DirTree, self).__init__()
        self.pathname = pathlib.Path(pathname)
        self.filename = filename
        self.tree = ''

    def set_path(self, pathname):
        self.pathname = pathlib.Path(pathname)

    def set_filename(self, filename):
        self.filename = filename

    def generate_tree(self, n=0):
        if self.pathname.is_file():  # is_file() 判断是否为文件
            self.tree += '    |' * n + '-' * 4 + self.pathname.name + '\n'
        elif self.pathname.is_dir():  # is_dir() 判断是否为目录
            self.tree += '    |' * n + '-' * 4 + \
                         str(self.pathname.relative_to(self.pathname.parent)) + '\\' + '\n'

            for cp in self.pathname.iterdir():  # iterdir() 返回一个迭代器，包含所有文件夹和文件
                self.pathname = pathlib.Path(cp)
                self.generate_tree(n + 1)

    def save_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.tree)


if __name__ == '__main__':
    dir_tree = DirTree()

    if len(sys.argv) == 1:  # 命令参数个数为1，生成当前目录的目录树
        dir_tree.set_path(pathlib.Path.cwd())  # Path.cwd() 当前目录
        dir_tree.generate_tree()
        print(dir_tree.tree)
    elif len(sys.argv) == 2 and pathlib.Path(sys.argv[1]).exists():  # 在命令行中的指定目录
        dir_tree.set_path(sys.argv[1])
        dir_tree.generate_tree()
        print(dir_tree.tree)
    elif len(sys.argv) == 3 and pathlib.Path(sys.argv[1]).exists():  # 在命令行中的保存文件
        dir_tree.set_path(sys.argv[1])
        dir_tree.generate_tree()
        dir_tree.set_filename(sys.argv[2])
        dir_tree.save_file()
    else:
        print('参数错误，无法运行！')

# ### 标准库pathlib模块
# - Object-oriented filesystem paths
# - 官方文档：https://docs.python.org/3/library/pathlib.html
