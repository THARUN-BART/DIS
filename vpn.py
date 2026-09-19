import socket, threading, time

xor = lambda data: bytes(b ^ 123 for b in data)

def server():
    with socket.create_server(("localhost", 5000)) as s:
        c, _ = s.accept()
        print("Server:", xor(c.recv(1024)).decode())
        c.send(xor(b"Hello Secure Client!"))

def client():
    time.sleep(0.1)
    with socket.create_connection(("localhost", 5000)) as c:
        c.send(xor(b"Hello Secure Server!"))
        print("Client:", xor(c.recv(1024)).decode())

threading.Thread(target=server, daemon=True).start()
client()