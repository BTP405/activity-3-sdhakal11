import socket
import pickle

class Client:
    """
    A client class for sending tasks to a server.
    """
    def __init__(self, server_ip, server_port):
        """
        Initialize the client with the server's IP address and port number.
        """
        self.server_ip = server_ip
        self.server_port = server_port

    def send_task(self, task, args):
        """
        Sending a task to the server for processing.
        """
        # Creating a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Connecting to the server
                s.connect((self.server_ip, self.server_port))

                pickled_task = pickle.dumps((task, args))

                # Sending the pickled task to the server
                s.sendall(pickled_task)

                # Receiving the result from the server
                data = s.recv(1024)
                result = pickle.loads(data)
                return result
            except Exception as e:
                print(f"An error occurred: {e}")
