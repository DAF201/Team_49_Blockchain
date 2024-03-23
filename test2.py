import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 2025))
    s.listen()
    conn, addr = s.accept()
    data = ''
    while True:
        data = conn.recv(1024)
        if data == b'':
            break
        print(data)
        conn.sendall(data)
