import socket
'''
tcp需要先启动server端
获取服务端执行命令输出在终端的结果
'''
tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("127.0.0.1", 10000))
while 1:
    while 1:
        data = input('>>>').strip()
        tcpclient.send(data.encode('utf-8'))

        ret = tcpclient.recv(1024)

        print(ret.decode('gbk'))
