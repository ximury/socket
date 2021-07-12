# 循环接收发送信息
# tcp需要先启动server端
import pprint
import socket
import ssl
import OpenSSL.crypto as crypto

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslcon = ssl.wrap_socket(tcpclient,
                         keyfile='../sslinfo/client_rsa_private.pem',
                         certfile='../sslinfo/client.crt',
                         server_side=False)
sslcon.connect(("127.0.0.1", 9011))

print(pprint.pformat(sslcon.getpeercert(True)))
cert_bin = sslcon.getpeercert(True)    # 服务端的证书信息
x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_bin)
print("CN=" + x509.get_subject().CN)

while 1:
    while 1:
        data = input('>>>').strip()

        sslcon.send(data.encode('utf-8'))

        ret = sslcon.recv(1024)

        print(ret.decode('utf-8'))
