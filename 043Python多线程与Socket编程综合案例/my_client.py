"""
客户端程序通过查询服务器获知某个数字是否为素数。
"""
import socket

while True:
    data = input('Input an integer(q to quit):').strip()
    if not data:
        continue
    if data == "q":
        break
    if data.isdigit():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(("127.0.0.1", 5005))
        except:
            print("server not found")
            exit(0)

        sock.sendall(data.encode())
        print(sock.recv(100).decode())

    sock.close
