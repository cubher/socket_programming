import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        message = input("Enter message to send (type 'quit' to exit): ")
        client_socket.sendall(message.encode('utf-8'))

        if message.lower() == 'quit':
            break

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received echo from server: {data}")

    client_socket.close()
    print("Connection with server closed.")

if __name__ == "__main__":
    host = '127.0.0.1'  # Replace this with your server's IP address
    port = 16002       # Replace this with your desired port number
    start_client(host, port)
