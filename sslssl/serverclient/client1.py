# 循环接收发送信息
# tcp需要先启动server端
import socket

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("127.0.0.1", 9011))
while 1:
    while 1:
        data = input('>>>').strip()

        tcpclient.send(data.encode('utf-8'))

        ret = tcpclient.recv(1024)

        print(ret.decode('utf-8'))
