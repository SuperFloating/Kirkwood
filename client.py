import socket
import json
# import socket.timeout as TimeoutException

# local host
# UDP_IP = '127.0.0.1'
# aws host
with open('credential.json') as c:
	credential = json.load(c)
UDP_IP = credential['server_ip']
UDP_PORT = credential['server_port']
BUFFER = 4096
MSG = ""
with open('template.json') as f:
	data_in_json = json.load(f)
# print(data_in_json)
MSG = json.dumps(data_in_json)

UDP_IP = '127.0.0.1'
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MSG)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
sock.sendto(MSG.encode('utf-8'), (UDP_IP, UDP_PORT))

data = ''
try:
	data, server = sock.recvfrom(BUFFER)
except socket.timeout:
	print("Timeout!")
if data != '':
	print(data.decode('utf-8'))
sock.close()

