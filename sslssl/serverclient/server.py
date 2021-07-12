# 循环接收发送信息
# tcp需要先启动server端, 关闭时需要先关闭client端
import pprint
import socket
import ssl

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = ssl.wrap_socket(tcpserver,
                       ca_certs='./ca.crt',
                       keyfile='./server_rsa_private.pem',
                       certfile='./server.crt',
                       cert_reqs=ssl.CERT_REQUIRED,
                       server_side=True)
# ca_certs: 用这个根证书校验客户端上传过来的证书是否可信任
# cert_reqs=sslssl.CERT_REQUIRED: 客户端必须要带自己的证书过来，即公钥，如果单向认证，cert_reqs,ca_certs两个参数没有
# server_side=True: 表示是服务端，必须参数

print(serv.context.get_ca_certs(binary_form=False))

serv.bind(("127.0.0.1", 9012))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    print('conn: ', conn)
    while True:
        try:
            data = conn.recv(1024)
            print(data.decode("utf-8"))

            try:
                serv.getpeercert()
            except Exception as e:
                print(e)

            ret_data = "OK, starting..."
            conn.send(ret_data.encode('utf-8'))

        except Exception:
            break
    conn.close()
