import socket

ser_soc = socket.socket()
ser_soc.bind((socket.gethostname(), 8723))

ser_soc.listen(5)
print("Waiting for any client request !")
clt, adr = ser_soc.accept()

print("Connection created with client: ", adr)

while True:
    data = clt.recv(1024).decode()
    if data == "bye":
        break
    print("From Client: ", data)

    data = input("=>")
    clt.send(data.encode())
    
ser_soc.close()
