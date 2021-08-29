import socket

clt_soc = socket.socket()
clt_soc.connect((socket.gethostname(), 8723))

msg = input("=>")

while True:
    clt_soc.send(msg.encode())

    data = clt_soc.recv(1024).decode()
    print("From server: ", data)

    msg = input("=>")

clt_soc.close()
