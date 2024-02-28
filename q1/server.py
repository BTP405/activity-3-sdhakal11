import socket
import pickle
import os

def receive_file(directory, server_ip, server_port):
    """
    Receives a file and saves it to the given directory.

    """
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print("Directory is not valid.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Binding to the given IP and port
            s.bind((server_ip, server_port))

            # Listening for connections
            s.listen()

            # Accepting a connection
            conn, addr = s.accept()

            with conn:
                print('Connected by', addr)

                # Receiving pickled file data
                pickled_file_data = conn.recv(1024)

                # Unpickling file data
                file_data = pickle.loads(pickled_file_data)

                # Writing file data to disk
                with open(os.path.join(directory, 'received_file'), 'wb') as f:
                    f.write(file_data)
                print("File received and saved successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
