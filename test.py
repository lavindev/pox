
import socket
import time
UDP_IP = "10.0.0.5"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDPi
while True:
	for i in range(0, 10000):
		sock.sendto(MESSAGE, (UDP_IP, 1000+i))
	

