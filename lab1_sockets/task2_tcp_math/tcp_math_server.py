import socket
import math


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(1)

print("TCP сервер запущен")

connection, address = server.accept()
print("Клиент подключился:", address)

data = connection.recv(1024).decode("utf-8")
a, b = map(float, data.split())
c = math.sqrt(a ** 2 + b ** 2)

answer = f"Гипотенуза равна {c}"
connection.send(answer.encode("utf-8"))

connection.close()
server.close()
