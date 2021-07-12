读取私钥文件 ca_rsa_private.pem 时不需要输入密码，亦即不对私钥进行加密存储，
那么将`-passout pass:123456`替换成`-nodes`

不带密码

`
$openssl req -newkey rsa:2048 -nodes -keyout privkey.pem -x509 -days 365 -out certificate.pem
`

带密码

`
openssl req -newkey rsa:2048 -passout pass:123456 -keyout nprivkey.pem -x509 -days 365 -out ncertificate.pem
`

参考文献

`
https://blog.csdn.net/ccj15010192778/article/details/103646988
`

查看证书细节信息

`
openssl x509 -text -noout -in ca.crt
`

使用 CA 证书来分别校验由自己颁发的
服务器证书 server.crt 和客户端证书 client.crt

`
openssl verify -CAfile ca.crt server.crt
`

双向认证
```
serv = ssl.wrap_socket(tcpserver,
                       ca_certs='./ca.crt',
                       keyfile='./server_rsa_private.pem',
                       certfile='./server.crt',
                       cert_reqs=ssl.CERT_REQUIRED,
                       server_side=True)
sslcon = ssl.wrap_socket(tcpclient,
                         ca_certs='./ca.crt',
                         keyfile='./client_rsa_private.pem',
                         certfile='./client.crt',
                         cert_reqs=ssl.CERT_REQUIRED,
                         server_side=False)
```

单向认证
```
serv = ssl.wrap_socket(tcpserver,
                       keyfile='./server_rsa_private.pem',
                       certfile='./server.crt',
                       server_side=True)
sslcon = ssl.wrap_socket(tcpclient,
                         ca_certs='./ca.crt',
                         cert_reqs=ssl.CERT_REQUIRED,
                         server_side=False)
```