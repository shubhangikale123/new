import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='LocalHost'

port= 5300
s.bind((host,port))
s.listen(5)

while True:
    c, address = s.accept()
    #n = c.recv(2048)
    #n = int(n)
    #e = c.recv(2048)
    #e = int(e)
    n, e = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved public key from client is n=%d,e=%d\n", (n,e))
    m=input("enter your message ")
    if int(m):
        k=(m**e)%n

    print("Encrypted data send is %d\n", k)
    c.send(str(k))
    c.close()
