# 循环接收发送信息
# tcp需要先启动server端
import socket
import time

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind(("", 9012))
tcpserver.listen(5)
# 当有两个连接建立的时候，如果其中有一个客户端连接断开，另一个会立即取得连接，进行通信
while True:
    conn, addr = tcpserver.accept()
    print(conn)
    # 循环发送接收消息
    while True:
        try:
            data = conn.recv(1024)
            print(data.decode("utf-8"))
            time.sleep(3)
            ret_data = "OK, starting..."
            # conn.send(data.upper())
            conn.send(ret_data.encode('utf-8'))

            # is_finished = input('>>>').strip()
            # conn.send(is_finished.encode('utf-8'))
        except Exception as e:
            print(e)
            break
    conn.close()
# tcpserver.close()
