
import socket
import threading
import smtplib 
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1) 
port = 7868
ip= "192.168.43.179"
s.bind((ip,port))
s.listen()

def program(session ,addr):
    print(addr)
    session.send(b"i am server" )
    cilent_id = session.recv(100).decode()
    cilent_sub = session.recv(100).decode()
    data=session.recv(100).decode()
    email=                                 										 # mail id by which you want to login 
    password=																									 # App password which created in mail account 
    print(cilent_id +"\n " + cilent_sub + "\n"+ data)
    smtp_object.login(email,password)
    from_id =                                                  # mail id by which you want to send msg (login id )
    to = cilent_id
    subject = cilent_sub
    message =data
    msg= "subject : " + subject + " \n "+ " message : "+message
    smtp_object.sendmail(from_id , to , msg )
while True:
    session,addr = s.accept()
    t1= threading.Thread(target = program , args=(session , addr))
    t1.start()
