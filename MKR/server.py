import socket
import struct
import numpy as np
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'  # Локальний хост
PORT = 65432  # Порт для прослуховування


def handle_client(client_socket, address):
    try:
        print(f"[INFO] Підключено клієнта: {address}")

        # Приймаємо розміри матриць
        sizes_data = client_socket.recv(12)  # 12 байтів для трьох int
        N, M, L = struct.unpack('iii', sizes_data)
        print(f"[INFO] Отримано розміри матриць: N={N}, M={M}, L={L}")

        if N <= 0 or M <= 0 or L <= 0:
            raise ValueError("Розміри матриць повинні бути додатніми числами.")

        # Приймаємо матриці
        print("[INFO] Очікується отримання матриць...")
        matrix_a = np.frombuffer(client_socket.recv(N * M * 4), dtype=np.float32).reshape((N, M))
        matrix_b = np.frombuffer(client_socket.recv(M * L * 4), dtype=np.float32).reshape((M, L))
        print("[INFO] Матриці отримані.")

        # Множення матриць
        print("[INFO] Виконується множення матриць...")
        result = np.dot(matrix_a, matrix_b)

        # Відправляємо результат назад клієнту
        client_socket.sendall(result.astype(np.float32).tobytes())
        print(f"[INFO] Результат відправлено клієнту: {address}")

    except Exception as e:
        print(f"[ERROR] Помилка: {e}")
    finally:
        client_socket.close()
        print(f"[INFO] З'єднання з клієнтом {address} закрито.")


# Основна функція сервера
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"[INFO] Сервер запущено, прослуховування {HOST}:{PORT}")

        with ThreadPoolExecutor(max_workers=5) as executor:
            while True:
                client_socket, address = server_socket.accept()
                executor.submit(handle_client, client_socket, address)


if __name__ == "__main__":
    main()
