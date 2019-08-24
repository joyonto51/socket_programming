import socket
import pickle

self_ip_address = "127.0.0.1"
server_ip_address = "127.0.0.1"
c2_port = 3458
s2_port = 3459

c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c2.connect((server_ip_address, c2_port))

def run_server():
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind((self_ip_address, s2_port))
    s2.listen(5)

    clt, adr = s2.accept()
    print("Connection to {} established".format(adr))

    return clt

clt = run_server()


while True:
    my_msg = c2.recv(160)

    dict = pickle.loads(my_msg)

    print(dict)


    "================="

    m = input("message: ")
    my_msg = pickle.dumps(m)

    clt.send(my_msg)

