'''import socket 
s = socket.socket()
s.connect(("127.0.0.1", 12345))
print(s.recv(1024).decode())
s.close
'''



import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 12345))
    s.sendall(b"Hellow")
    data = s.recv(1024)
print(data)