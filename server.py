import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(BUFFER)
	print(addr)
	print(data.decode('utf-8'))
	# print("receive from: " + addr)
	# print("received message: " + data.decode('utf-8'))