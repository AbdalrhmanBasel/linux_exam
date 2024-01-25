# 1. Create CLI application.
# 2. Client request the server's IP from user.
# 3. Client connects to server on port 1303 using IP address recieved from user.
# 4. Client reads string from server and close connection and exit.

import socket

class TimeClient:
    def __init__(self):
        self.SERVER_PORT = 1303

    def start_client(self):
        server_ip = input("Enter the server's IP address (Ex: 127.0.0.1): ")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((server_ip, self.SERVER_PORT))
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {data}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    time_client = TimeClient()
    time_client.start_client()
