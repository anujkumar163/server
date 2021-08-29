import socket

clt_soc = socket.socket()
clt_soc.connect((socket.gethostname(), 8723))

data = clt_soc.recv(1024)
ser_msg = data.decode("utf-8")
print(ser_msg)
