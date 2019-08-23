import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1030))
s.listen(5)

while True:
	clt, adr = s.accept()

	print("Connection to {} established".format(adr))

	message = str(input("message : "))
	clt.send(bytes(message))
	clt.close()
