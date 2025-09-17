import socket
import random

P,G=23,5

s=socket.socket()

host='0.0.0.0'
port=12345

a=random.randint(2,P-2)
A=pow(G,a,P)

with s:
    s.bind((host,port))
    s.listen(1)
    print("Server Listening")
    
    c,addr=s.accept()
    
    with c:
        print(f"Server connected to {addr}")
        c.sendall(str(A).encode()+b'\n')
        
        B=int(c.recv(1024).decode().strip())
        
        shared = pow(B,a,P)
        
        print(f"Shared key {shared}")
        c.sendall(b"Ok\n")
    
        