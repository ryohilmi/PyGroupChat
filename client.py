import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(bytes("Hi server", "utf-8"), ("127.0.0.1", 2209))

message, address = s.recvfrom(1024)

print(message.decode("utf-8"))