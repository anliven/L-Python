#! python3
# -*- coding: utf-8 -*-
import logging
import Chapter01_logging05_b as moduleB  # 导入其他模块
import yaml
import logging.config
import os


def setup_logging(default_path='config.yaml', default_level=logging.INFO):  # 读取yaml文件的配置
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)  # 通过dictConfig()方法将配置项传给logging模块进行全局初始化
    else:
        logging.basicConfig(level=default_level)


def log_a():
    logging.debug('Module A - Debug')
    logging.info('Module A - Info')


if __name__ == '__main__':
    config_file_path = 'Chapter01_logging05_config.yaml'
    setup_logging(config_file_path)
    log_a()
    moduleB.log_b()  # 调用导入模块的run()方法

# ### 配置文件共享
# 将配置存放于专门的配置文件中，可以被多个模块所使用，也便于管理和维护；
# 格式简洁的YAML文件适用于编写配置文件，比JSON更为方便；
#
# ### 主入口文件
# 主入口文件对应配置文件中root一项配置；
#
# ### pyyaml
# http://pyyaml.org/wiki/PyYAML
# https://pypi.org/project/PyYAML/
