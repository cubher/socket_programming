import socket as s
import select as sel

HOST = ""
PORT = 4444
SOCKET_LIST = []
RECEIVE_BUFF = 4096

def chat_server():
	server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
	server_socket.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
	server_socket.bind((HOST,PORT))
	server_socket.listen()
	SOCKET_LIST.append(server_socket)

	print("LAHTP chat server stated on port"+str(PORT)+"....")

	while True:
		#blocking the flow for new incoming connection ..
		ready_read, ready_write, error = sel.select(SOCKET_LIST,[],[],0)
		#after getting new connection
		for sock in ready_read:
			#checking the same obj
			if sock == server_socket:
				client_socket, addr = server_socket.accept()
				SOCKET_LIST.append(sockfd)
				print("client "+addr+" connection,")
				broadcast(server_socket, client_socket, "{} entered our chat room.. \n".format(addr))
			else:
				try:
					data = sock.recv(RECEIVE_BUFF)
					if data:
						broadcast(server_socket, sock, "{} entered our chat room.. \n".format(addr))
						pass
					else:
						#the socket mmust have been broken,remove it from the list
						if sock in SOCKET_LIST:
							SOCKET_LIST.remove(sock)
						#TODO: Broadcast thaat the someone has disconnected
				except:
					#TODO: Broadcast that some one disconnected
					continue
			#TODO:  plan to exit
			#server_socket.close()

def broadcast(server_socket,client_socket,message):
	for socket in SOCKET_LIST:
		if socket != server_socket and socket != client_socket:
			try:
				socket.send(message)
			except:
				socket.close()
				if socket in SOCKET_LIST:
					SOCKET_LIST.remove(socket)