import socket
import random
from threading import Thread
from datetime import datetime
from time import sleep

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

socket = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
socket.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
name = input("Enter your name: ")
socket.send(name.encode())

def listen_for_messages():
    try:
        while True:
            message = socket.recv(1024).decode()
            print("\n" + message)
    except Exception as e:
        print(f"Error listening: {e}")

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

def print_usage():
    print("Welcome to Yapping Corner!")
    print("Operations Menu:")
    print("\t/enter <channel name> -> enter a channel.")
    print("\t/leave -> leave the curernt channel.")
    print("\t/info -> display name and curernt channel.")
    print("\t/channels -> display all the channels.")
    print("\t/private <user name> -> private talk with another user.")
    print("\t/quit -> exit the program.")

print_usage()

while True:
    data = input(f"{name} >> ")
    cmd = data.strip().lower()

    if cmd == '/quit':
        socket.send(cmd.encode())
        break

    if cmd == "/channels" or cmd[:6] == "/enter" or cmd == "/leave" or cmd == "/info" or cmd[:8] == "/private":
        socket.send(cmd.encode())
    
    else:
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        data = f"[{date_now}] {name}{separator_token}{data}"
        socket.send(data.encode())

    sleep(0.5)

socket.close()