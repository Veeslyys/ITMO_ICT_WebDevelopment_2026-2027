import socket
import threading


clients = []


def send_all(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            send_all(message, client)
        except:
            break

    clients.remove(client)
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5002))
server.listen()

print("Сервер чата запущен")

while True:
    client, address = server.accept()
    clients.append(client)
    print("Подключился пользователь:", address)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
