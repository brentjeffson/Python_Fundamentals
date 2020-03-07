from chat import Chat
import threading
import time

def start_server():
    clients = []
    server = Chat.create_server()

    def remove_client(client):
        for clt, addrs in clients:
            if client[0] == clt:
                index = clients.index(client)
                clients.pop(index)
                print(f'Client {addrs} disconnected.')
                return

    def start_thread(client):
        clt, addrs = client
        print(f'Thread started for {addrs}')
        
        while True:
            try:
                msg = Chat.receive_message(clt)
                print(f'Client:{addrs}: {msg}', end='\n')

                if msg == '\exit()':
                    clt.close()
                    remove_client(client)
                    return
                broadcast(client, msg)
            except Exception as e:
                print(f'{e.with_traceback}')
                remove_client(client)
                clt.close()
                break
        
    def broadcast(client, msg):
        for clt, addrs in clients:
            if client[0] == clt:
                continue
            print(f'{addrs}')
            Chat.send_message(clt, f'{client[1]}: {msg}')


    server.listen(2)
    while True:
        print('Waiting for connection...')
        clt, addrs = server.accept()
        clients.append((clt, addrs))
        print(f'Connection Established with {addrs}')
        Chat.send_message(clt, 'Welcome, You are now connected to the server.')
        
        threading.Thread(target=start_thread, args=[(clt, addrs)], daemon=True).start()


if __name__ == '__main__':
    start_server()









