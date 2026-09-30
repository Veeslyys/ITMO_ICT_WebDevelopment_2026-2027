# Лабораторная работа 1. Сокеты

## Задание 1

Файлы:

- `task1_udp/udp_server.py`
- `task1_udp/udp_client.py`

Сначала запускается сервер, потом клиент.

```bash
python3 udp_server.py
python3 udp_client.py
```

Клиент отправляет сообщение `Hello, server`, сервер выводит его и отправляет ответ `Hello, client`.

## Задание 2

Файлы:

- `task2_tcp_math/tcp_math_server.py`
- `task2_tcp_math/tcp_math_client.py`

Вариант: теорема Пифагора.

```bash
python3 tcp_math_server.py
python3 tcp_math_client.py
```

Клиент вводит два катета, сервер считает гипотенузу и отправляет результат клиенту.

## Задание 3

Файлы:

- `task3_http_file/http_server.py`
- `task3_http_file/index.html`

```bash
python3 http_server.py
```

После запуска нужно открыть в браузере:

```text
http://127.0.0.1:8080
```

Сервер отправляет браузеру HTML-страницу из файла `index.html`.

## Задание 4

Файлы:

- `task4_chat/chat_server.py`
- `task4_chat/chat_client.py`

```bash
python3 chat_server.py
python3 chat_client.py
```

Для проверки нужно открыть несколько клиентов в разных терминалах. Сообщение одного клиента отправляется остальным клиентам. Используются `socket`, TCP и `threading`.

## Задание 5

Файл:

- `task5_web_grades/web_grades_server.py`

```bash
python3 web_grades_server.py
```

После запуска нужно открыть:

```text
http://127.0.0.1:8081
```

Сервер обрабатывает GET и POST запросы. Через форму можно добавить дисциплину и оценку, после этого они выводятся на странице.
