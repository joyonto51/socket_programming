import socket
import pickle

c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c2.connect((socket.gethostname(), 2247))

def run_server():
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind((socket.gethostname(), 2248))
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

