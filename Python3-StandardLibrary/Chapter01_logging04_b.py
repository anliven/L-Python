# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('mA.mB')  # 特别注意：这里开头的“mA”是主入口文件中的Logger名称


def log_b():
    logger.info('Module B - Info')
    logger.debug('Module B - Debug')
    logger.error('Module B - Error')


if __name__ == '__main__':
    log_b()

# ### 复用Logger配置
# 使用主入口文件中的Logger名称来创建logger，就会复用主入口文件中的Logger配置；
