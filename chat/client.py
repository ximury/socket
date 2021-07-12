# 循环接收发送信息
# tcp需要先启动server端
import socket
import time

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("192.168.240.136", 9012))
while 1:
    while 1:
        # please open vncserver
        data = input('>>>').strip()

        tcpclient.send(data.encode('utf-8'))

        time.sleep(3)
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
