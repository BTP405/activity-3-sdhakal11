import socket
import pickle
import os

def send_file(file_path, server_ip, server_port):
    """
    Sends a file over a socket connection to a server.
    """
    # Making sure the file exists
    if not os.path.isfile(file_path):
        print("File path is not valid.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connecting to server
            s.connect((server_ip, server_port))

            # Reading the file
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Pickle file data
            pickled_file_data = pickle.dumps(file_data)

            # Send pickled file data
            s.sendall(pickled_file_data)
            print("File sent successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
