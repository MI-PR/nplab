import socket
import random

s=socket.socket()

host='127.0.0.1'
port=12345

P,G=23,5

b=random.randint(2,P-2)
B=pow(G,b,P)

with s:
    s.connect((host,port))
    print(f"Client connected to {port}")
    
    A=int(s.recv(1024).decode().strip())
    s.sendall(str(B).encode()+b'\n')
    
    shared=pow(A,b,P)
    print(f"Shared key is {shared}")
    print(f"Server replied {s.recv(1024).decode().strip()}")