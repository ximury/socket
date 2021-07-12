import socket

'''
循环发送接收消息
udp是无链接的，先启动哪一端都不会报错
'''
ip_port = ('127.0.0.1', 10001)
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    msg, addr = udp_client.recvfrom(1024)
    print(msg.decode('utf-8'), addr)
    if msg.decode('utf-8') == 'Q':
        print("quiting...")
