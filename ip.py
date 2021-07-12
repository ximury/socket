import socket


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        ip = '127.0.0.1'
        print(e)
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    print(get_host_ip())
