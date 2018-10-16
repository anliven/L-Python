# -*- coding: utf-8 -*-
import logging
import sys
import Chapter14_logging04_b as mB  # 导入其他模块

logger = logging.getLogger('mA')  # 定义Logger的名称
logger.setLevel(level=logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == '__main__':
    logger.info('Module A - Info')
    logger.debug('Module A - Debug')
    logger.error('Module A - Error')
    mB.log_b()  # 调用导入模块的方法

# ### 配置共享
# 父子模块共享配置机制：可以根据Logger的名称来自动加载父模块的配置；
# 子模块只需要在定义Logger对象时，将父模块的Logger名称作为Logger名称开头即可；
