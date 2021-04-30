import socket, threading

def receieve_data(sock, receieved_packets):
  while True:
    data, address = sock.recvfrom(1024)
    receieved_packets.add((data, address))

def run_server():
  host = "127.0.0.1"
  port = 2209

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((host, port))

  clients = set()
  receieved_packets = set()

  recv_thread = threading.Thread(target=receieve_data, args=(s, receieved_packets))
  recv_thread.start()

  while True:
    if len(receieved_packets) != 0:
      data, address = receieved_packets.pop()

      clients.add(address)

      data = data.decode("utf-8")
      print(data)

      for client in clients:
        if client != address:
          s.sendto(data.encode("utf-8"), client)

run_server()