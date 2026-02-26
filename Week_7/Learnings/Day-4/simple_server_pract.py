import socket
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #used to create TCP socket

server.bind(("127.0.0.1", 8080)) #attach this socket to ip 127.0.0.1,8080, now this program owns it

server.listen(5) #listen for connections

print("Server running on http://127.0.0.1:8080")

while True:
    conn, addr = server.accept()
    time.sleep(10)
    print("connected by:", addr)
    
    request = conn.recv(4096)
    
    if not request:
        conn.close()
        continue
    
    print("Raw Request:")
    print(request.decode())
    
    body = "Hello from raw socket server"
    
    response = (
        "HTTP/ 1.1 200 OK\r\n"
        "Content-Type:text/plain\r\n"
        f"Content-Length:{len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )
    
    conn.send(response.encode())
    conn.close()
    