import socket
import threading


name = input("Введите имя: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5002))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            break


thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    text = input()
    message = name + ": " + text
    client.send(message.encode("utf-8"))
