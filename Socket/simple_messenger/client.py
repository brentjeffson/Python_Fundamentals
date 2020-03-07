from chat import Chat
import threading

def start_client():
    
    connected = True
    client = Chat.create_client()
    client.connect(('localhost', 1024))
    msg = Chat.receive_message(client)
    print(msg)

    def receiver_thread(client):
        try:
            while connected:
                msg = Chat.receive_message(client)
                print(msg)
            print('Disconnected From Server.')
        except ConnectionResetError as e:
            print(f'Error: Server Closed Connection.')
            return
    
    threading.Thread(target=receiver_thread, args=[client], daemon=True).start()

    while connected:
        try:
            msg = input('>')
            Chat.send_message(client, msg)
            if msg == '\exit()':
                connected = False
        except ConnectionResetError as e:
            print(f'Error: Server Closed Connection.')
            connected = False




if __name__ == '__main__':
    start_client()