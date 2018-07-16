#! python3
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info('Start')
logger.warning('Something maybe fail.')
try:
    result = 10 / 0
except Exception as e:
    # logging.error('Error: %s', e)  # 直接使用字符串格式化方法输出错误（不包含Traceback信息）
    # logger.error('Failed to get result', exc_info=True)  # error()方法中的exc_info参数
    logging.exception('Failed to get result')  # 直接使用exception()方法
logger.info('Finished')

# ### Traceback
# 详细的Traceback信息，便于调试程序和排查异常；
# 直接使用字符串格式化方法输出错误（不包含Traceback信息）；
# 输出Traceback信息：
# - 方法1：将error()方法中的exc_info参数设置为True，可以输出执行过程中的信息（完整的Traceback信息）；
# - 方法2：直接使用exception()方法；
