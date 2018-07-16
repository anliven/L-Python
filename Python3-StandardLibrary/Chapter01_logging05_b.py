#! python3
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('mA.mB')  # 使用配置文件中定义的Logger名称


def log_b():
    logger.info('Module B - Info')
    logger.debug('Module B - Debug')
    logger.error('Module B - Error')


if __name__ == '__main__':
    log_b()
