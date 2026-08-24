import socket
import sys
from concurrent.futures import ThreadPoolExecutor


with ThreadPoolExecutor() as executor:
    s = socket.socket()

    s.bind(("127.0.0.1", 12345))
    s.listen(5)
    data = "super"
    while True:
        c, addr = s.accept()
        print(f"connection is succed by{addr}")
        while data != "q":
            data = c.recv(1024)
            print(data)
        else:
            c.send('thanks for connecting'.encode())
            c.close()
