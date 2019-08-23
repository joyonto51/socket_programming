import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1030))

message_info = ""

while True:
	msg = s.recv(5)

	print(msg)
	if len(msg) <= 0:
		break

	message_info += msg


print(message_info)
