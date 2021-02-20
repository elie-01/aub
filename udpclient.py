import socket
import datetime

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = "127.0.0.1"
port = 50051

for i in range (0,5):
	msg = input("Send to server: ")
	T1 = datetime.datetime.now()
	s.sendto(bytes(msg,"utf-8"),(IP,port))
	data , addr = s.recvfrom(1024)
	T2 = datetime.datetime.now()
	T3 = T2 - T1
	print("data: ",str(data),"RTT = ",T3)
	
   
s.close()
