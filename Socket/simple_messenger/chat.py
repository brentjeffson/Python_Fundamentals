import socket




class Chat():

    @staticmethod
    def create_server(address=('localhost', 1024)):
        '''Create a tcp socket server
            Args:
                address (tuple(str, int)): Address to bind the socket into.
            Returns:
                s (socket): Socket object

        '''

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(address)

        return s

    @staticmethod
    def create_client():
        '''Create client socket object
            Returns:
                s (socket): Socket object
        '''

        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    @staticmethod
    def send_message(s, msg, encoding='utf-8'):
        '''Send a message to `s`.
            
            Args:
                s (socket): socket object to send message to.
                msg (str): message sent to socket object.
            Returns:
                no value
        '''
        s.send(bytes(msg, encoding=encoding))

    @staticmethod
    def receive_message(s, chunk=1024, encoding='utf-8'):
        '''Receives a message from `s` socket object.

            Args:
                s (socket): socket object to receive from.
                chunk (int): number of bytes to received.
                encoding (str): encoding used to decode the message.

            Returns:
                msg (str): decoded message
        '''

        msg = s.recv(chunk)
        return msg.decode(encoding)


