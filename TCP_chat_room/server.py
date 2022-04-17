#!/usr/bin/env python3

import threading
import socket
from sys import argv

if len(argv) != 2:
    print("Usage: ./server.py [PORT]")
    exit(1)

HOST = "127.0.0.1"  # localhost
try:
    PORT = int(argv[1])     # free port
    if PORT < 0 or str(PORT) != argv[1]:
        raise ValueError
except ValueError:
    print("PORT must be a whole, positive number")
    exit(1)


server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((HOST, PORT))
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
            if not msg:
                raise Exception
            broadcast(msg)
        except Exception:
            i = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[i]
            print(f"{nickname}: connection lost")
            broadcast(f"{nickname} has left the chat")
            nicknames.pop(i)
            print(nicknames)
            print(clients)
            break


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
