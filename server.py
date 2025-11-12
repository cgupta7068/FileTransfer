import socket
import os

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

def send_file(conn, filename):
    try:
        with open(f'files/{filename}', 'rb') as f:
            while chunk := f.read(1024):
                conn.sendall(chunk)
        print(f"File {filename} sent successfully.")
    except FileNotFoundError:
        print("File not found.")
        conn.sendall(b"File not found")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        filename = conn.recv(1024).decode()
        send_file(conn, filename)
