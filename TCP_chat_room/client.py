#!/usr/bin/env python3

from threading import Thread
import socket
from sys import argv

if len(argv) != 2:
    print("Usage: ./client.py [PORT]")
    exit(1)

HOST = "127.0.0.1"  # localhost
try:
    PORT = int(argv[1])     # free port
    if PORT < 0 or str(PORT) != argv[1]:
        raise ValueError
except ValueError:
    print("PORT must be a whole, positive number")
    exit(1)

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((HOST, PORT))    # server connection

nickname: str = "unknown"


def receive():
    """Listening to server messages"""
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            if msg == "Your nickname: ":
                global nickname
                nickname = input(msg)
                client.send(nickname.encode("ascii"))
            else:
                print(msg)
        except:
            print("An ERROR occurred")
            client.close()
            break


def write():
    """Write new message into the chat"""
    while True:
        msg = input()
        client.send(f"{nickname}: {msg}".encode("ascii"))


recv_thread = Thread(target=receive)
recv_thread.start()
write_thread = Thread(target=write)
write_thread.start()
