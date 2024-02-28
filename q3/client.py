import socket
import pickle
import threading

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        pickled_message = pickle.dumps(message)
        self.client_socket.send(pickled_message)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024)
                print(pickle.loads(message))
            except Exception as e:
                print(f"An error occurred: {e}")
                self.client_socket.close()
                break
