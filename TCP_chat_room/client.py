#!/usr/bin/env python3

from threading import Thread
import socket
from sys import argv

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(("127.0.0.1", int(argv[1])))    # server connection
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
        except Exception:
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
