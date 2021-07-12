import socket
import subprocess

'''
tcp需要先启动server端
获取服务端执行命令输出在终端的结果
'''

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind(("127.0.0.1", 10000))
tcpserver.listen(5)
while True:
    conn, addr = tcpserver.accept()
    print(conn)
    while True:
        try:
            data = conn.recv(1024)
            ret = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            error = ret.stderr.read()
            if error:
                cmd_ret = error
            else:
                cmd_ret = ret.stdout.read()
            conn.send(cmd_ret)
        except Exception:
            break
    conn.close()
tcpserver.close()
