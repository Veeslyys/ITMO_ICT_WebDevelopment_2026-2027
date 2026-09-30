import socket
from urllib.parse import parse_qs


grades = []


def make_page():
    rows = ""
    for subject, grade in grades:
        rows += f"<li>{subject}: {grade}</li>"

    return f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Оценки</title>
</head>
<body>
    <h1>Оценки по дисциплинам</h1>
    <form method="POST">
        <p>Дисциплина: <input name="subject"></p>
        <p>Оценка: <input name="grade"></p>
        <button type="submit">Добавить</button>
    </form>
    <h2>Список оценок</h2>
    <ul>{rows}</ul>
</body>
</html>
"""


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8081))
server.listen(5)

print("Веб-сервер запущен: http://127.0.0.1:8081")

while True:
    connection, address = server.accept()
    request = connection.recv(4096).decode("utf-8")

    if request.startswith("POST"):
        body = request.split("\r\n\r\n")[1]
        data = parse_qs(body)
        subject = data.get("subject", [""])[0]
        grade = data.get("grade", [""])[0]
        if subject and grade:
            grades.append((subject, grade))

    html = make_page()
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html; charset=utf-8\r\n\r\n"
    response += html

    connection.send(response.encode("utf-8"))
    connection.close()
