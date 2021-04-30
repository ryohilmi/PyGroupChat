import socket, threading

def receieve_data(sock):
  while True:
    try:
      data, address = sock.recvfrom(1024)
      print(data.decode("utf-8"))
    except:
      pass

def run_client():
  host = "127.0.0.1"
  port = 2209

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  name = input("Insert your name here : ")

  recv_thread = threading.Thread(target=receieve_data, args=(s, ))
  recv_thread.start()

  while True:
    message = input()

    data = f"{name} : {message}"

    s.sendto(data.encode("utf-8"), (host, port))

run_client()