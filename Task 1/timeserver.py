# Create CLI Server & Run It On Linux.
# Server opens on port 1303 for listening.
# When client connect is established - send string with date and time
# After connection is closed, server must wait for connetion from client


import socket
import datetime

class TimeServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)

        print(f"Server is listening on port {self.port}...")

        try:
            while True:
                client_socket, client_address = server_socket.accept()
                self.handle_client(client_socket)
        except KeyboardInterrupt:
            print("\nServer interrupted. Closing...")

    def handle_client(self, client_socket):
        current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        client_socket.send(current_time.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    time_server = TimeServer(host='0.0.0.0', port=1303)
    time_server.start_server()
