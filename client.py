import socket

HOST = '127.0.0.1'  # Server address
PORT = 65432        # Port to connect to

filename = input("Enter filename to request: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(filename.encode())
    with open(f'received/{filename}', 'wb') as f:
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            f.write(chunk)
    print(f"File {filename} received and saved.")
