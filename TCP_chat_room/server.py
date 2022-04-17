#!/usr/bin/env python3

import threading
import socket
from sys import argv

host = "127.0.0.1"  # localhost
port = int(argv[1])  # free port

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients: list[socket] = []
nicknames: list[str] = []


def broadcast(msg: str):
    """Broadcasting message to all connected clients"""
    msg = msg.encode("ascii")   # encoding message
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            broadcast(msg)
        except Exception:
            i = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[i]
            broadcast(f"{nickname} has left the chat")
            nicknames.pop(i)


def receive():
    while True:
        client, address = server.accept()
        print(f"New connection: {address}")
        client.send("Your nickname: ".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Client{address} nickname: {nickname}")
        client.send(f"Connected to the chatroom".encode("ascii"))
        broadcast(f"{nickname} joined the chat room")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Listening for connections...")
receive()
print("Server connection ended")
