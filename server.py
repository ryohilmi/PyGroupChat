import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 2209))

while True:
  message, address = s.recvfrom(1024)

  print(f"Message : {message.decode('utf-8')} \nAddress: {address}")

  s.sendto(bytes("Connected to the server", "utf-8"), address)
