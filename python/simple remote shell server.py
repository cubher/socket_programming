import socket as s
import select as sel

HOST = "127.0.0.1"
PORT = 16002


def echo_server():
    with s.socket(s.AF_INET, s.SOCK_STREAM) as server_sock:
        host_address = (HOST, PORT)
        server_sock.bind(host_address)
        server_sock.listen()
        while True:

                client_sock, client_address = server_sock.accept()
                print(f"client has conneted ({client_address})")
                while True:
                    data = client_sock.recv(1084).decode("utf-8")
                    if not data :
                        print("nothing")
                        break
                    print(f"Received message from client: {data}")
                    if data.lower() == "quit":
                        client_sock.sendall(b"Connection terminated. Goodbye!")
                        break
                    else :
                        client_sock.sendall(data.encode("utf-8"))
        

if __name__ == "__main__":
    echo_server()
    print(f"Connection with {HOST} closed.")