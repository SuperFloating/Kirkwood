import socket
import json
from datetime import datetime

import perform_action
import parse_request as pr

UDP_IP = ''
UDP_PORT = 8080
BUFFER = 4096
RESP = 'hello from the server!'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (UDP_IP, UDP_PORT)
sock.bind(server_addr)

while True:
	data, addr = sock.recvfrom(BUFFER)
	data = data.decode('utf-8')

	if data:

		now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		print(now)
		print(str(addr), '\n', str(data))

		sent = sock.sendto(RESP.encode('utf-8'), addr)
		print("response sent!")
		
		# performs actions
		data_in_json = json.loads(data)
		pr.parse_request(data_in_json)

		print('\n')
