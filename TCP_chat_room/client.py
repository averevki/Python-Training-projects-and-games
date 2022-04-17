#!/usr/bin/env python3

from sys import argv
import socket
from threading import Thread, Lock

if len(argv) > 2:
    print("Usage: ./client.py [PORT]")
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

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect((HOST, PORT))    # server connection

nickname: str = "unknown"
STOP_THREAD = False


def receive():
    """Listening to server messages"""
    global STOP_THREAD
    while True:
        if STOP_THREAD is True:
            break
        try:
            msg = client.recv(1024).decode("utf-8")
            if msg == "Your nickname: ":
                write_lock.acquire()
                global nickname
                nickname = input(msg)
                client.send(nickname.encode("utf-8"))
                nxt_msg = client.recv(1024).decode("utf-8")
                if nxt_msg == "Password: ":
                    client.send(input(nxt_msg).encode("utf-8"))
                    if client.recv(1024).decode("utf-8") == "Wrong password":
                        print("Wrong password")
                        STOP_THREAD = True
                else:
                    print(nxt_msg)
                    if nxt_msg == "You are BANNED":
                        client.close()
                        STOP_THREAD = True
                write_lock.release()
            else:
                print(msg)
        except Exception:
            print("An ERROR occurred")
            client.close()
            break


def write():
    """Write new message into the chat"""
    write_lock.acquire()    # wait for authentication
    while True:
        if STOP_THREAD:
            break
        msg = input()
        if msg.startswith("/"):
            client.send(msg.encode("utf-8"))
        else:
            client.send(f"{nickname}: {msg}".encode("utf-8"))


write_lock = Lock()     # authorization lock

recv_thread = Thread(target=receive)
recv_thread.start()
write_thread = Thread(target=write)
write_thread.start()
