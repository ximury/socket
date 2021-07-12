import socket

'''
循环发送接收消息
udp是无链接的，先启动哪一端都不会报错
'''
ip_port = ('127.0.0.1', 10001)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)
while True:
    msg, addr = udp_server.recvfrom(1024)
    print(msg, addr)
    udp_server.sendto(msg.upper(), addr)
    if msg.decode('utf-8') == 'q':
        print("quiting...")
        udp_server.close()
