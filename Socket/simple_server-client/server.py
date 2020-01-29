import socket


def server():
    print('Creating Server...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1024))

    s.listen(2)
    while True:
        print('Waiting for connection...')
        client, addrs = s.accept()
        print(f'Connection to {addrs} established.')
        client.send(bytes('Socket Programming in Python', 'utf-8'))

    s.close()
if __name__ == '__main__':
    server()