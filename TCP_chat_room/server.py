#!/usr/bin/env python3

from sys import argv
import socket
import threading

if len(argv) > 2:
    print("Usage: ./server.py [PORT]")
    exit(1)

HOST = "127.0.0.1"  # localhost
PORT = 54321    # standard port
if len(argv) == 2:
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

clients: list[socket.socket] = []
nicknames: list[str] = []


def broadcast(msg: str):
    """Send message to all connected clients"""
    msg = msg.encode("utf-8")   # encoding message
    for client in clients:
        client.send(msg)


def handle(client: socket.socket):
    """Receiving users messages"""
    while True:
        try:
            msg: str = client.recv(1024).decode("utf-8")
            if not msg:
                raise ConnectionError
            if msg.startswith("/"):
                if nicknames[clients.index(client)] == "admin":
                    if msg.startswith("/kick "):
                            nickname = msg[6:]
                            if nickname in nicknames:
                                broadcast(f"{nickname} was KICKED by admin")
                                kick_user(nickname)
                    elif msg.startswith("/ban "):
                        if nicknames[clients.index(client)] == "admin":
                            nickname = msg[5:]
                            if nickname in nicknames:
                                broadcast(f"{nickname} was BANNED by admin")
                                kick_user(nickname)
                            with open("bans.txt", "a") as f:
                                f.write(nickname + "\n")
                else:
                    client.send("Insufficient permissions".encode("utf-8"))
            else:
                broadcast(msg)
        except Exception:
            i = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[i]
            print(f"{nickname}: connection lost")
            broadcast(f"{nickname} has left the chat")
            nicknames.pop(i)
            break


def receive():
    """
    Listening for new connections and
    assigning for them threads"""
    while True:
        client, address = server.accept()
        print(f"New connection: {address}")

        client.send("Your nickname: ".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")

        with open("bans.txt", "r") as f:
            banned = f.read().splitlines()
        if nickname in banned:
            client.send("You are BANNED".encode("utf-8"))
            client.close()
            continue

        if nickname == "admin":
            client.send("Password: ".encode("utf-8"))
            password = client.recv(1024).decode("utf-8")

            if password != "admin":
                client.send("Wrong password".encode("utf-8"))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)
        print(f"Client{address} nickname: {nickname}")

        client.send(f"Connected to the chatroom".encode("utf-8"))
        broadcast(f"{nickname} joined the chat room")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_user(nickname: str):
    """Kick user from server by his nickname"""
    i = nicknames.index(nickname)
    client_to_kick = clients.pop(i)
    client_to_kick.send("Server connection lost".encode("utf-8"))
    client_to_kick.close()
    nicknames.pop(i)


print("Listening for connections...")
receive()
print("Server connection ended")
