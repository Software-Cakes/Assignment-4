import socket
from threading import Thread

clients = set()
channels = {}

class Client:
  def __init__(self, socket, address, name):
    self.socket = socket
    self.address = address
    self.name = name
    self.channel = None
    self.direct_user = None
  def __str__(self):
    return f"{self.socket}, {self.address}: ({self.name})"
  def send(self, msg):
    self.socket.send(msg.encode())
  def currentChannelName(self):
    if self.channel:
        return self.channel.name
    else:
        return ""
  def enter_channel(self, channel):
    self.channel = channel
    self.direct_user = None
  def enter_direct_mode(self, direct_user):
    self.channel = None
    self.direct_user = direct_user
  def is_in_channel(self):
    return self.channel != None
  def is_in_direct_mode(self):
    return self.direct_user != None
  def leave(self):
    self.channel = None
    self.direct_user = None

def findClient(name):
    for c in clients:
        if c.name == name:
            return c
    return None

class Channel:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"{self.name}"

def listChannels():
    s = ""
    i = 1
    for ch in channels.values():
        print(ch.name)
        s = s + f"{i}. {ch.name}\n"
        i += 1
    if s:
        return s
    else:
        return "NO channels!"

def findChannel(name, create_new):
    for ch in channels.values():
        if (ch.name == name):
            return ch

    if create_new:
        new_channel = Channel(name)
        channels[name] = new_channel
        return new_channel
    return None

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT}")

def broadcast(client, msg):
    for c in clients:
        if c.name != client.name and c.channel and c.channel.name == client.channel.name:
            c.send(msg.replace(separator_token, ": "))

def send_direct_message(client, msg):
    anotherClient = findClient(client.direct_user)
    if anotherClient:
        anotherClient.send(msg.replace(separator_token, ": "))

def listen_for_client(client):
    while True:
        try:
            msg = client.socket.recv(1024).decode()
            cmd = msg.strip().lower()

            if cmd == '/quit':
                print(f"{client.name} quited")
                break
            elif cmd == "/channels":
                client.send(listChannels())

            elif cmd[:6].lower() == "/enter":
                channel_name = msg[-(len(msg) - 6):].strip()
                client.enter_channel(findChannel(channel_name, True))
                print(f"{client.name} entered channel {client.channel.name}")
                client.send(f"Entered {client.channel.name}.")

            elif cmd[:8].lower() == "/private":
                s = msg[-(len(msg) - 8):].strip()
                another_client = findClient(s)
                if another_client:
                    client.enter_direct_mode(another_client.name)
                    another_client.enter_direct_mode(client.name)

                    client.send(f"You have entered a private chat with {another_client.name}.")
                    another_client.send(f"You have entered a private chat with {client.name}.")

                    print(f"{client.name} has entered a private chat with {another_client.name}")
                else:
                    client.send(f"Cannot find the user {s}")
                    print(f"Cannot find the user {s}")

            elif cmd == "/leave":
                if client.is_in_channel():
                    s = client.channel.name
                    client.leave()
                    client.send(f"You have left channel {s}.")
                    print(f"{client.name} has left channel {s}")
                elif client.is_in_direct_mode():
                    s = client.direct_user
                    client.leave()
                    client.send(f"Left user {s}")
                else:
                    client.send("You have yet to enter a channel or in private chat.")

            elif cmd == "/info":
                if client.is_in_channel():
                    client.send(f"Your nickname: {client.name}\nJoined Channel: {client.currentChannelName()}")
                elif client.is_in_direct_mode():
                    client.send(f"You are now in private chat with {client.direct_user}.")
                else:
                    client.send(f"Your nickname: {client.name}")

            else:
                if client.is_in_channel():
                    broadcast(client, msg)
                elif client.is_in_direct_mode():
                    send_direct_message(client, msg)
                else:
                    client.send("You need to eneter a channel or in a private chat first!")

        except Exception as e:
            print(f"[!] Error: {e}")
            break

    client.socket.close()
    clients.remove(client)

while True:
    socket, address = server_socket.accept()
    print(f"{address} connected.")

    name = socket.recv(100).decode()
    new_client = Client(socket, address, name)
    clients.add(new_client)

    t = Thread(target=listen_for_client, args=(new_client,))
    t.daemon = True
    t.start()

for c in clients:
    c.socket.close()
server_socket.close()