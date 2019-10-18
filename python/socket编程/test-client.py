#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''''
'''
1.使用while True 实现客户端服务端循环通信
2.if not msg:continue  判断是否有消息 防止空消息问题
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等同于服务端
s.connect(('127.0.0.1',10010))     #拨通电话 注意此处是一个元组的形式

while True:
    msg = raw_input('>>:').strip()
    if not msg:
        continue
    s.send(msg)
    # 转为二进制发出去
    # s.send(msg.encode('utf-8'))
    print('ready to recv message')
    # 接收消息
    backmsg = s.recv(1024)
    print backmsg
    # print(backmsg.decode('utf-8'))

s.close()