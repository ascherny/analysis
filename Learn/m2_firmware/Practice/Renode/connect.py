#!/usr/bin/env python3
import socket

HOST = "127.0.0.1"  # localhost
PORT = 12345  # target port

s = socket.create_connection((HOST, PORT))
s.send(b"Wubba Lubba Dub Dub!!!!!!!!!!!!!")

response = b""
while True:
    data = s.recv(1)
    response += data
    if data == b"\x00":
        break

print("Received {}".format(response))
s.close()
