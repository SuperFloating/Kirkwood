import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
BUFFER = 1024
MSG = 'hihi'

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MSG)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MSG.encode('utf-8'), (UDP_IP, UDP_PORT))


data, server = sock.recvfrom(BUFFER)
print(data.decode('utf-8'))
sock.close()

