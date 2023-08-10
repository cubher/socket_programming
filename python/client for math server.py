import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to math server")
    data = client_socket.recv(1024).decode()
    print(data)
    while True:
        message = input()
        client_socket.sendall(message.encode())

        if message.lower() == 'quit':
            break

        data = client_socket.recv(1024).decode()
        print(f"{data}")

    client_socket.close()
    print("Connection with server closed.")

if __name__ == "__main__":
    host = '127.0.0.1'  # Replace this with your server's IP address
    port = 3075       # Replace this with your desired port number
    start_client(host, port)
