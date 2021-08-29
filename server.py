import socket
server_socket = socket.socket()
server_socket.bind((socket.gethostname(), 4354))

server_socket.listen(4)
clt, adr = server_socket.accept()
print("connection created:", adr)
