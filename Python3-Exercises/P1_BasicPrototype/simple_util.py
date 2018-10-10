# coding=utf-8


def lines(file):
    """文本块生成器lines：在文件末尾添加一个空行"""
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    """文本块生成器blocks：收集所有非空行来生成文本块，得到一个表示文本块的字符串"""
    block = []
    for line in lines(file):
        if line.strip():  # 删除多余的空白
            block.append(line)  # 将其包含的所有行合并
        elif block:
            yield ''.join(block).strip()  # 删除多余的空白
            block = []
