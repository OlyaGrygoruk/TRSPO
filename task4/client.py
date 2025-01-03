import socket  # Імпортуємо модуль socket


def start_client(host='127.0.0.1', port=65432):
    # 1. Створюємо TCP-сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 2. Підключаємося до сервера
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # 3. Чекаємо введення повідомлення від користувача
            message = input("Enter message to send (type 'exit' to quit): ")
            if message.lower() == 'exit':  # Вихід із програми
                break

            # 4. Відправляємо повідомлення серверу
            client_socket.sendall(message.encode())  # Перетворюємо рядок у байти

            # 5. Отримуємо відповідь від сервера
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")  # Декодуємо байти в рядок


if __name__ == "__main__":
    start_client()
