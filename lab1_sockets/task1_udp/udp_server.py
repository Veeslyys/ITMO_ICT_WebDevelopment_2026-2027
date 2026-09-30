import socket


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))

print("UDP сервер запущен")

data, address = server.recvfrom(1024)
message = data.decode("utf-8")
print("Сообщение от клиента:", message)

server.sendto("Hello, client".encode("utf-8"), address)
server.close()
