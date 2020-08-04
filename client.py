import socket
import json

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
BUFFER = 4096

with open('test.json') as f:
	json_data = json.load(f)

# print(json_data)
MSG = str(json_data)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MSG)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MSG.encode('utf-8'), (UDP_IP, UDP_PORT))


data, server = sock.recvfrom(BUFFER)
print(data.decode('utf-8'))
sock.close()

