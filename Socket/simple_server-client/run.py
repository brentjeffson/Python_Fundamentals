import client
import server
import threading
import time

server_thread = threading.Thread(target=server.server)
client_thread = threading.Thread(target=client.client)

server_thread.start()
time.sleep(3)
client_thread.start()





