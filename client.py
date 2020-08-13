import socket
import json

# local host
# UDP_IP = '127.0.0.1'
# aws host
UDP_IP = '34.212.178.87'
UDP_PORT = 8080
BUFFER = 4096

MSG = ""
with open('template.json') as f:
	data_in_json = json.load(f)

# print(data_in_json)
MSG = json.dumps(data_in_json)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MSG)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MSG.encode('utf-8'), (UDP_IP, UDP_PORT))

data, server = sock.recvfrom(BUFFER)
print(data.decode('utf-8'))
sock.close()

