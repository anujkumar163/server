import socket

ser_soc = socket.socket()
ser_soc.bind((socket.gethostname(), 8723))

ser_soc.listen(5)
print("Waiting for any client request !")
clt, adr = ser_soc.accept()

print("Connection created with client: ", adr)

msg = input("Enter Msg: ")
clt.send(bytes(msg, "utf-8"))