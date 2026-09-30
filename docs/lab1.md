# ЛР1. Работа с сокетами

## Цель работы

Изучить основы работы с библиотекой `socket` в Python и реализовать простые клиент-серверные приложения с использованием протоколов UDP, TCP и HTTP.

## Структура проекта

```text
lab1_sockets/
├── task1_udp/
│   ├── udp_server.py
│   └── udp_client.py
├── task2_tcp_math/
│   ├── tcp_math_server.py
│   └── tcp_math_client.py
├── task3_http_file/
│   ├── http_server.py
│   └── index.html
├── task4_chat/
│   ├── chat_server.py
│   └── chat_client.py
├── task5_web_grades/
│   └── web_grades_server.py
├── README.md
└── report.txt
```

## Задание 1. UDP клиент и сервер

Реализованы UDP-сервер и UDP-клиент. Клиент отправляет сообщение `Hello, server`, сервер принимает его, выводит в консоль и отправляет ответ `Hello, client`.

Файлы:

- `lab1_sockets/task1_udp/udp_server.py`
- `lab1_sockets/task1_udp/udp_client.py`

Запуск:

```bash
cd lab1_sockets/task1_udp
python3 udp_server.py
python3 udp_client.py
```

## Задание 2. TCP вычисление гипотенузы

Реализованы TCP-сервер и TCP-клиент для вычисления гипотенузы по теореме Пифагора. Клиент вводит два катета, отправляет их серверу, сервер выполняет вычисление и возвращает результат.

Файлы:

- `lab1_sockets/task2_tcp_math/tcp_math_server.py`
- `lab1_sockets/task2_tcp_math/tcp_math_client.py`

Запуск:

```bash
cd lab1_sockets/task2_tcp_math
python3 tcp_math_server.py
python3 tcp_math_client.py
```

## Задание 3. Простой HTTP-сервер

Реализован HTTP-сервер, который при подключении клиента отправляет HTML-страницу из файла `index.html`.

Файлы:

- `lab1_sockets/task3_http_file/http_server.py`
- `lab1_sockets/task3_http_file/index.html`

Запуск:

```bash
cd lab1_sockets/task3_http_file
python3 http_server.py
```

После запуска страница доступна по адресу:

```text
http://127.0.0.1:8080
```

## Задание 4. Многопользовательский чат

Реализован многопользовательский TCP-чат. Сервер принимает несколько подключений, создает отдельный поток для каждого клиента и пересылает сообщения другим участникам.

Файлы:

- `lab1_sockets/task4_chat/chat_server.py`
- `lab1_sockets/task4_chat/chat_client.py`

Запуск:

```bash
cd lab1_sockets/task4_chat
python3 chat_server.py
python3 chat_client.py
```

Для проверки можно открыть несколько клиентов в разных терминалах.

## Задание 5. Web-сервер оценок

Реализован простой web-сервер, который обрабатывает GET и POST-запросы. Через HTML-форму можно добавить дисциплину и оценку, после чего данные отображаются на странице.

Файл:

- `lab1_sockets/task5_web_grades/web_grades_server.py`

Запуск:

```bash
cd lab1_sockets/task5_web_grades
python3 web_grades_server.py
```

После запуска страница доступна по адресу:

```text
http://127.0.0.1:8081
```

## Вывод

В ходе лабораторной работы были реализованы UDP и TCP клиент-серверные приложения, простой HTTP-сервер, многопользовательский чат с потоками и web-сервер для обработки GET/POST-запросов. Работа демонстрирует базовые принципы сетевого взаимодействия и обработки клиентских подключений средствами Python.
