import socket

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立
tcpserver.bind(("127.0.0.1", 10000))  # 绑定
tcpserver.listen(5)  # 监听
conn, addr = tcpserver.accept()  # 阻塞等待连接
data = conn.recv(1024)  # 接收
print(data.decode("utf-8"))
conn.send(data.upper())  # 发送
conn.close()  # 关闭连接
tcpserver.close()  # 关闭
