# 循环接收发送信息
# tcp需要先启动server端
import socket
import ssl

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = ssl.wrap_socket(tcpserver, keyfile='./privkey.pem', certfile='./certificate.pem', server_side=True)
serv.bind(("", 9011))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    print(conn)
    while True:
        try:
            data = conn.recv(1024)
            print(data.decode("utf-8"))
            ret_data = "OK, starting..."

            conn.send(ret_data.encode('utf-8'))

        except Exception:
            break
    conn.close()
