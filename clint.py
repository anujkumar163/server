import socket
cnt_socket = socket.socket()
cnt_socket.connect((socket.gethostname(), 4354))
