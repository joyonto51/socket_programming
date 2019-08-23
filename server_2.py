import socket
import pickle

a = 10
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((socket.gethostname(), 2247))
s1.listen(5)

def get_response():
    c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c1.connect((socket.gethostname(), 2248))

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

