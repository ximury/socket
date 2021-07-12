import base64
from Crypto.Hash import SHA3_256 as SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS

message = "This is the message to send."
rsa_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDdcwUnRJmkMljsQOgBPHQ/cxbq2jV7D6MR/7X4yNS3wxgqnvkC
8dLEXXN9LogOWGafOTo+kQzENNWaLaYEAaYrKeyGz5qXkk+RqmgZUnGS/soHE0xy
ltuC4uIuzABo7BsS0OfryA9OMIWMAYa8WnhX54Fg7rAsm4yq88d1LFgMRQIDAQAB
AoGAC6l7rf5jhk14eAilrzBQgZQ9XWTcctH3U9f+7KPMQAPa3p5nSAvAKRiFdSQ2
2g/hvPo14lxKgH1fz7IeZLue1TH2jh47lxeNaeFREoYh98Bdi38ed0TcH4L2EBmK
WdoiJu2FxGq7SS4JMYxFbUwDJ2zZE6X1rITmWOu3+j3We4kCQQDfhwcvK4bHxS0n
zdF4Eg/vSXScI/UebHF80e/cFA9uXT3PWgddU/o3dCLNxRAIwA/RZ0ECSm8dH4Hv
smEqQ1l3AkEA/Z60oKc9p/AaVMqOIViY/c1T9iWxMfbHfXwQ4TQMBHEOo4x2dCYx
5zBlrnehPBO0ugoQ9lZsv+6h3ZfsqPf3IwJALiWYTBq2VqPUcLVDG4DPHV2S33Fk
94T34QcOd+cEUIqbaiVyA8iEjdJCJS0b5FKScW7Zsvle+yo4Dx5KhQkmfQJBALk2
UUqRV6Fw4onRcoI/pVqTvCEh3YlTYtPs6pbL34rO1ZXyWf7wdbkTyu3iR0kMSwsh
lsmOy9ROfL7K1/V9QGkCQC7f6ynqm+ODnVocfZJmze0KAhSD9RKOnVLOcOEtcf0K
45WELzbo03nzkN64DaBxdviw8+mEV5jikEF1tdejMc0=
-----END RSA PRIVATE KEY-----"""

rsa_pub = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdcwUnRJmkMljsQOgBPHQ/cxbq
2jV7D6MR/7X4yNS3wxgqnvkC8dLEXXN9LogOWGafOTo+kQzENNWaLaYEAaYrKeyG
z5qXkk+RqmgZUnGS/soHE0xyltuC4uIuzABo7BsS0OfryA9OMIWMAYa8WnhX54Fg
7rAsm4yq88d1LFgMRQIDAQAB
-----END PUBLIC KEY-----"""

# 数据签名
with open('test/rsa.key', 'r') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    signer = PKCS1_PSS.new(rsa_key_obj)
    # 先以单向加密方式通过某种哈希算法（如MD5，SHA1等）对要发送的数据生成摘要信息（数据指纹）
    digest = SHA.new()
    digest.update(message.encode())
    # 然后发送方用自己密钥对中的私钥对这个摘要信息进行加密，生成签名信息
    signature = base64.b64encode(signer.sign(digest))
    print('signature info: ', signature)

# rsa_key_obj = RSA.importKey(rsa_key)
# signer = PKCS1_PSS.new(rsa_key_obj)
# # 先以单向加密方式通过某种哈希算法（如MD5，SHA1等）对要发送的数据生成摘要信息（数据指纹）
# digest = SHA1.new()
# digest.update(message.encode('utf-8'))
# # 然后发送方用自己密钥对儿中的私钥对这个摘要信息进行加密，生成签名信息
# signature = base64.b64encode(signer.sign(digest))
# print('signature info: ', signature)

# 验证签名, NEED: message,signature
with open('test/rsa.pub', 'r') as f:
    # signature = b'B2tUB33iOHmAyJ5QuS6JBMYtcti1FvBMYeiTkgFYWts32z2+RD5bsvwaqo33axJhm6iKfRR2KOn5OT5WktZ0Z5fZWQ8RgqWtKiNgDUfmZ3rxxOyr5injHxhIfsVCq1J3lnrVYTsWG7mxUsruHJbwJPNfrGGMOmeBxredUsD2vKs='
    print(signature)
    public_key = f.read()
    # 数据接收方用发送的公钥对加密后的摘要信息进行解密，得到数据摘要的明文A
    rsa_key_obj = RSA.importKey(public_key)
    signer = PKCS1_PSS.new(rsa_key_obj)
    # 数据接收方再通过相同的哈希算法计算得到数据摘要信息B
    digest = SHA.new(message.encode())
    # 对比数据摘要A与数据摘要B，如果两者一致说明数据没有被篡改过
    is_ok = signer.verify(digest, base64.b64decode(signature))
    print(base64.b64decode(signature))
    print('is ok: ', is_ok)

# message = 'This is the message to send..'
# signature = b'tWKsdGDc172nyH9jMTzQhsVFh8lHsdAhathR+6g1M21xnN3qmVHAjhzldsy78Mv+lmMEK+gPPgBM+DAOyKxR+NwH7l2Ec8nQQ8pcJiSscb/5Q2adOVmoDQWFJVnQpEfK2pV1FoT5EMMwWuzaQ8AzFYHLTvU5UldZOHPuaecUmkQ='
# rsa_key_obj = RSA.importKey(rsa_pub)
# signer = PKCS1_PSS.new(rsa_key_obj)
# # 数据接收方再通过相同的哈希算法计算得到数据摘要信息B
# digest = SHA1.new(message.encode('utf-8'))
# # 对比数据摘要A与数据摘要B，如果两者一致说明数据没有被篡改过
# is_ok = signer.verify(digest, base64.b64decode(signature))
# print('is ok: ', is_ok)