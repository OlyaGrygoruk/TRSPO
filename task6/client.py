import socket
import struct

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        for i in range(100):  # Відправляємо 100 повідомлень
            # Формуємо різнотипні повідомлення
            if i % 2 == 0:
                message = f"Text message {i}"  # Текстове повідомлення
            else:
                message = f"Number: {i}"  # Числове повідомлення у вигляді тексту

            message_bytes = message.encode()
            message_length = len(message_bytes)

            # Відправляємо заголовок і повідомлення
            client_socket.sendall(struct.pack('!I', message_length))  # Заголовок
            client_socket.sendall(message_bytes)  # Основне повідомлення

            # Отримуємо відповідь від сервера
            header = client_socket.recv(4)  # Отримуємо заголовок
            response_length = struct.unpack('!I', header)[0]  # Декодуємо довжину
            response = client_socket.recv(response_length).decode()  # Отримуємо відповідь
            print(f"Server response: {response}")

if __name__ == "__main__":
    start_client()
