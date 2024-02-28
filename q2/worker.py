import socket
import pickle
import multiprocessing

class Worker:
    """
    A worker class for processing tasks received from a client.
    """
    def __init__(self, worker_ip, worker_port):
        """
        Initialize the worker with its IP address and port number.
        """
        self.worker_ip = worker_ip
        self.worker_port = worker_port

    def start(self):
        """
        Start the worker to listen for incoming connections.
        """
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind the socket to the worker's IP address and port number
            s.bind((self.worker_ip, self.worker_port))

            # Listen for incoming connections
            s.listen()

            while True:
                # Accept a connection
                conn, addr = s.accept()

                # Create a new process to handle the client
                process = multiprocessing.Process(target=self.handle_client, args=(conn, addr))
                process.start()

    def handle_client(self, conn, addr):
        """
        Handle a client connection.
        """
        try:
            # Receive the pickled task from the client
            data = conn.recv(1024)

            # Unpickle the task and its arguments
            task, args = pickle.loads(data)
            result = task(*args)
            pickled_result = pickle.dumps(result)

            conn.sendall(pickled_result)
        except Exception as e:
            print(f"An error occurred: {e}")
