# 循环接收发送信息
# tcp需要先启动server端
import socket
import ssl

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslcon = ssl.wrap_socket(tcpclient, keyfile='./privkey.pem', certfile='./certificate.pem', server_side=False)
sslcon.connect(("172.17.4.202", 9011))
while 1:
    while 1:
        data = input('>>>').strip()

        sslcon.send(data.encode('utf-8'))

        ret = sslcon.recv(1024)

        print(ret.decode('utf-8'))
