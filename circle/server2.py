# 循环接收发送信息
# tcp需要先启动server端
import socket

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind(("172.17.4.202", 9012))
tcpserver.listen(5)

conn, addr = tcpserver.accept()
print(conn)
while True:
	try:
		data = conn.recv(1024)
		print(data.decode("utf-8"))
		ret_data = "OK, starting..."
		# conn.send(data.upper())
		conn.send(ret_data.encode('utf-8'))
		break
# is_finished = input('>>>').strip()
# conn.send(is_finished.encode('utf-8'))
	except Exception:
		break
conn.close()
# tcpserver.close()
