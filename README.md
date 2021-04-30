# Python UDP Group Chat

A simple group chat application made with Python3 and socket. It uses UDP (User Datagram) as its network protocol.

The program is split into two files: `server.py` and `client.py`. `server.py` server file handles all the clients' connections and sends the messages. `client.py` is used as an interface for the user to send the chats. Both use `socket` and `threading` package from Python3.

## Server

`server.py` has 2 main function, these are `run_server` and `receive_data`. Let's take a look inside the `run_server` function first.

```python
host = "127.0.0.1"
port = 2209

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
```

Initially, the socket is initialized with socket constructor. It is given 2 arguments: the family and protocol. I used `AF_INET` for the family and `SOCK_DGRAM` for the protocol one. AF_INET stands for IPv4 while SOCK_DGRAM stands for User Datagram Protocol. Then, the socket is binded with chosen host and port. 127.0.0.1 is localhost, and the port is arbitrary.

```python
clients = set()
received_packets = set()
```

After binding the socket, 2 sets are created to contain all clients' addresses and receieved_packets to be processed.

```python
recv_thread = threading.Thread(target=receieve_data, args=(s, received_packets))
recv_thread.start()
```

I made a thread called `recv_thread` to run the `receive_data` function without blocking the main loop.

```python
while True:
  if len(received_packets) != 0:
    data, address = received_packets.pop()

    clients.add(address)

    data = data.decode("utf-8")
    print(data)

    for client in clients:
      if client != address:
        s.sendto(data.encode("utf-8"), client)
```

And in the main loop, the program will process the received packets, add new clients to the set, and send the message to all other clients.

```python
def receieve_data(sock, receieved_packets):
  while True:
    data, address = sock.recvfrom(1024)
    receieved_packets.add((data, address))
```

Every new receieved packets will be added to the set by `receieve_data` function

## Client

Not that different with `server.py`, `client.py` has `receive_data` and `run_client` function.

```python
host = "127.0.0.1"
port = 2209

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Insert your name here : ")

recv_thread = threading.Thread(target=receieve_data, args=(s, ))
  recv_thread.start()
```

The initialization is basically the same, but without the binding process and the user will be prompted to input their username. It also runs a thread to recieve the data.

```python
while True:
  message = input()

  data = f"{name} : {message}"

  s.sendto(data.encode("utf-8"), (host, port))
```

In the main loop, the user will be prompted to input the message, and the message will be sent to the server and other users.

```python
def receieve_data(sock):
  while True:
    try:
      data, address = sock.recvfrom(1024)
      print(data.decode("utf-8"))
    except:
      pass
```

The `receieve_data` function will receieve the message from the server and print the message.

## Program in action

1. Run the server:
   ```sh
   $ py server.py
   ```
2. Run the client and insert the username:
   ```sh
   $ py client.py
   $ Insert your name here : Ryo
   ```
3. Run the other client:
   ```sh
   $ py client.py
   $ Insert your name here : Hilmi
   ```
4. Enter your message, and then press enter:

   ```sh
   $ Insert your name here : Hilmi
   $ Hii
   ```

   The message should appear in other client's and server's terminal like this

   ```sh
   $ Hilmi : Hii
   ```
