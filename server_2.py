import socket
import pickle

a = 10
self_ip_address = "127.0.0.1"
server_ip_address = "127.0.0.1"
s1_port = 3466
c1_port = 3467

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((self_ip_address, s1_port))
s1.listen(5)

def get_response():
    c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c1.connect((server_ip_address, c1_port))

    return c1


while True:
    clt, adr = s1.accept()
    print("Connection to {} established".format(adr))
    c1 = get_response()

    while True:
        m = input("message: ")
        my_msg = pickle.dumps(m)

        clt.send(my_msg)

        "========================"

        my_msg = c1.recv(160)

        dict = pickle.loads(my_msg)

        print(dict)

