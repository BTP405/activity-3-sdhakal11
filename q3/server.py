import socket
import pickle
import threading

class Server:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.server_ip, self.server_port))
        self.server_socket.listen()
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, addr):
        while True:
            try:
                message = client_socket.recv(1024)
                self.broadcast(message, client_socket)
            except Exception as e:
                print(f"An error occurred: {e}")
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, sender_socket):
        for client_socket in self.clients:
            if client_socket != sender_socket:
                client_socket.send(message)
