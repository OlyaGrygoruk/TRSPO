import socket  # Імпортуємо модуль socket для роботи з мережами


def start_server(host='127.0.0.1', port=65432):
    # 1. Створюємо TCP-сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # socket.AF_INET - використовуємо IPv4
        # socket.SOCK_STREAM - створюємо сокет для TCP протоколу

        # 2. Прив'язуємо сокет до адреси та порту
        server_socket.bind((host, port))

        # 3. Сокет починає слухати підключення
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        # 4. Приймаємо з'єднання від клієнта
        conn, addr = server_socket.accept()  # conn - з'єднання, addr - адреса клієнта
        with conn:  # Використовуємо контекстний менеджер для роботи із з'єднанням
            print(f"Connected by {addr}")
            while True:
                # 5. Приймаємо дані від клієнта (макс. 1024 байти за раз)
                data = conn.recv(1024)
                if not data:  # Якщо дані порожні, клієнт завершив з'єднання
                    break
                print(f"Received: {data.decode()}")  # Декодуємо байти в рядок

                # 6. Відправляємо ті ж самі дані назад клієнту
                conn.sendall(data)


if __name__ == "__main__":
    start_server()
