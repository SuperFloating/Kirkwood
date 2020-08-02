import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
BUFFER = 1024
RESP = 'hello from the server!'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (UDP_IP, UDP_PORT)
sock.bind(server_addr)

while True:
	data, addr = sock.recvfrom(BUFFER)
	print(addr)
	print(data.decode('utf-8'))

	if data:
		sent = sock.sendto(RESP.encode('utf-8'), addr)
		print("response sent!")
		# sock.close()
	