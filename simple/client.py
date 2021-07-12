import socket

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("127.0.0.1", 10000))  # 连接
data = input(">:")
tcpclient.send(data.encode("utf-8"))  # 发送
ret = tcpclient.recv(1024)  # 接收
print(ret.decode("utf-8"))
tcpclient.close()
