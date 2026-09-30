import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(1)

print("HTTP сервер запущен: http://127.0.0.1:8080")

while True:
    connection, address = server.accept()
    request = connection.recv(1024).decode("utf-8")
    print(request.splitlines()[0])

    file = open("index.html", "r", encoding="utf-8")
    html = file.read()
    file.close()

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html; charset=utf-8\r\n\r\n"
    response += html

    connection.send(response.encode("utf-8"))
    connection.close()
