# -*- coding: utf-8 -*-
import paramiko


def ssh2_trans(ip, username, passwd, cmd):
    # paramiko.util.log_to_file('ssh_log')  # 设置日志，记录交互信息
    try:
        trans = paramiko.Transport((ip, 22))
        trans.connect(username=username, password=passwd)
        s = paramiko.SSHClient()
        s._transport = trans  # 将sshclient对象的transport指定为trans
        stdin, stdout, stderr = s.exec_command(cmd)
        print("### %s is OK." % ip)
        # print(stdout.read().decode())  # 输出内容比较少时，直接使用read读取出所有的输出
        for line in stdout.readlines():  # 输出内容比较多时，按行读取进行处理
            print('... ' + line.strip('\n'))  # 使用strip()处理结尾换行符
    except Exception:
        print("### %s is Error." % ip)
    finally:
        trans.close()


ssh2_trans("10.91.48.171", "root", "arthur", "w")  # 注意：实参均为字符串类型
ssh2_trans("10.91.48.172", "root", "arthur", "hostname;uptime")  # 通过分号分割多个命令

# ### paramiko示例
# 实现SSH登录并执行命令；
