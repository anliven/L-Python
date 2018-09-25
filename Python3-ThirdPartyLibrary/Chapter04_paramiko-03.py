# -*- coding: utf-8 -*-
import paramiko
import os
import datetime


def scp(server, username, passwd, remotefile, localfile, gp='get'):
    # paramiko.util.log_to_file('scp_log')  # 设置日志，记录交互信息
    s = paramiko.Transport((server, 22))
    s.connect(username=username, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(s)
    if gp == 'get':
        sftp.get(remotefile, localfile)  # 从SFTP服务器下载文件
    else:
        sftp.put(localfile, remotefile)  # 上传文件到SFTP服务器
    s.close()


def scp_dir(host, username, password, remote_dir, local_dir, gp='get'):
    # paramiko.util.log_to_file('scp_dir_log')  # 设置日志，记录交互信息
    t = paramiko.Transport((host, 22))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    if gp == 'get':
        files = sftp.listdir(remote_dir)
        print(datetime.datetime.now(), ' Beginning to download files from', host)
        for f in files:
            print(datetime.datetime.now(), ' Downloading file:', os.path.join(remote_dir, f))
            sftp.get(os.path.join(remote_dir, f), os.path.join(local_dir, f))  # 下载
        print(datetime.datetime.now(), ' Download files success.')
    elif gp == 'put':
        files = os.listdir(local_dir)  # os.listdir(path) 返回本地指定path下的文件和文件夹的名字列表
        print(datetime.datetime.now(), ' Beginning to upload files to', host)
        for f in files:
            print(datetime.datetime.now(), ' Uploading file:', os.path.join(local_dir, f))
            sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))  # 上传
        print(datetime.datetime.now(), ' Upload files success.')
    else:
        print("Error Parameter!")
    t.close()


scp('10.91.116.87', 'root', 'arthur', '/root/test.txt', 'newfile.txt')
scp('10.91.116.87', 'root', 'arthur', '/root/newtest.txt', 'newfile.txt', 'put')
scp_dir('10.91.116.87', 'root', 'arthur', '/root/test/', os.getcwd())
scp_dir('10.91.116.87', 'root', 'arthur', '/root/test/', os.getcwd(), 'put')

# ### paramiko示例
# 实现SFTP上传与下载；
