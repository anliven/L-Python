#! python3
# -*- coding: utf-8 -*-
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  # 通过communicate()方法输入
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# ### subprocess模块
# subprocess模块可以方便地启动一个子进程，然后控制其输入和输出；
#
# ### communicate()方法
# 如果子进程还需要输入，则可以通过communicate()方法输入;
# communicate(b'set q=mx\npython.org\nexit\n')相当于在命令行执行nslookup命令后手动输入“set q=mx”、“python.org”、“exit”命令；
