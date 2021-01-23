import socket
s= socket.socket()

server_ip= # ip addresh of server (which system you want to connect )
server_port = # port number server program

s.connect( (server_ip , server_port ))
print(s.recv(1000))
s.send(b"xyz@gmail.com")    # mail you want to send
s.send(b"subject")     # subject of mail
s.send(b"msg ")    #msg you want to send