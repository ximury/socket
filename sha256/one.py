import datetime
import hashlib
import base64
import hmac


# 获取格式GMT格式时间
def get_gmt_timestr():
    gmt_formate = '%a, %d %b %Y %H:%M:%S GMT'
    t = datetime.datetime.utcnow().strftime(gmt_formate)
    return t


# hmac_sha256加密
def get_hmac_sha256(message, secret):
    message = message.encode('utf-8')
    secret = secret.encode('utf-8')
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode("utf-8")
    return signature


# 计算sha256
def get_sha256(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    res = base64.b64encode(bytes.fromhex(sha256.hexdigest())).decode("utf-8")
    return res


def echo(data, secret):
    digest = "SHA-256=%s" % get_sha256(data)
    gmt_date = get_gmt_timestr()
    signature = get_hmac_sha256("x-date: %s\ndigest: %s" % (gmt_date, digest), secret)
    print(signature)


if __name__ == "__main__":
    echo("abcd", "your secret")
