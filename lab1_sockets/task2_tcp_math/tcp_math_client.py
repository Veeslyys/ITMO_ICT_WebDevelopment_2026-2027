import socket


a = input("Введите первый катет: ")
b = input("Введите второй катет: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

message = a + " " + b
client.send(message.encode("utf-8"))

data = client.recv(1024).decode("utf-8")
print("Ответ сервера:", data)

client.close()
