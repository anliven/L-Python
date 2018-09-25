# -*- coding: utf-8 -*-
import paramiko


def ssh2(ip, username, passwd, cmd):
    # paramiko.util.log_to_file('ssh_log')  # 设置日志，记录交互信息
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        s.connect(ip, 22, username, passwd)
        stdin, stdout, stderr = s.exec_command(cmd)
        print("### %s is OK." % ip)
        # print(stdout.read())  # 输出内容比较少时，直接使用read读取出所有的输出
        for line in stdout.readlines():  # 输出内容比较多时，按行读取进行处理
            print('... ' + line.strip('\n'))  # 使用strip()处理结尾换行符
    except Exception:
        print("### %s is Error." % ip)
    finally:
        s.close()


ssh2("10.91.116.87", "root", "arthur", "w")  # 注意：实参均为字符串类型
ssh2("10.91.116.88", "root", "arthur", "hostname;uptime")  # 通过分号分割多个命令

# ### paramiko
# - SSH2 protocol library.
# - Home Page: https://github.com/paramiko/paramiko/  http://www.paramiko.org/
# - Documentation: http://docs.paramiko.org/
#
# ### 连接方式
# -通过paramiko.SSHClient()函数；
# -通过paramiko.Transport()函数；
#
# ### 支持基于用户名密码和秘钥的登录方式
