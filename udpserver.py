import socket
import datetime


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = "127.0.0.1"
port = 50051
s.bind((IP,port))

while True:
        print("Waiting for client...")
        data , addr = s.recvfrom(1024)
        now = datetime.datetime.now()
        print ("Received Messages:",str(data)," from",addr)
        print (now.strftime("%d-%m-%Y %H:%M:%S"))
	s.sendto(data,addr)
