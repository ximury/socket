# 循环接收发送信息
# tcp需要先启动server端
import socket

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("192.168.240.136", 9011))
while 1:
    while 1:
        # please open vncserver
        data = input('>>>').strip()

        tcpclient.send(data.encode('utf-8'))

        ret = tcpclient.recv(1024)

        print(ret.decode('utf-8'))

        # tcpclient.close()

# data = input('>>>').strip()
#
# tcpclient.send(data.encode('utf-8'))
#
# ret = tcpclient.recv(1024)
#
# print(ret.decode('utf-8'))
#
# tcpclient.close()
