# coding=utf-8
import logging.config

logging.config.fileConfig('Chapter14_logging05.conf')  # 加载日志配置

logging.debug('debug message')
logging.info("info message")
logging.warning('warn message')
logging.error("error message")
logging.critical('critical message')


# ### 使用配置文件
# 可以将日志的配置保存在一个配置文件中，然后在主程序中使用logging.config.fileConfig()读取配置文件；
