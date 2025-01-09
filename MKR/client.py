import socket
import struct
import numpy as np

HOST = '127.0.0.1'  # Локальний хост
PORT = 65432        # Порт для з'єднання

def generate_matrix(rows, cols):
    """Генерація матриці з випадковими числами."""
    return np.random.rand(rows, cols).astype(np.float32)

def main():
    try:
        # Генерація розмірів матриць
        N = np.random.randint(1001, 1500)
        M = np.random.randint(1001, 1500)
        L = np.random.randint(1001, 1500)

        # Генерація двох матриць
        matrix_a = generate_matrix(N, M)
        matrix_b = generate_matrix(M, L)
        print(f"[INFO] Згенеровано матриці розмірами: A({N}x{M}), B({M}x{L})")

        # Підключення до сервера
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print(f"[INFO] Підключено до сервера ({HOST}, {PORT})")

            # Надсилання розмірів матриць
            sizes = struct.pack('iii', N, M, L)
            client_socket.sendall(sizes)
            print("[INFO] Розміри матриць відправлено серверу.")

            # Надсилання матриць
            client_socket.sendall(matrix_a.tobytes())
            client_socket.sendall(matrix_b.tobytes())
            print("[INFO] Матриці відправлено серверу.")

            # Отримання результату від сервера
            result_data = client_socket.recv(N * L * 4)
            result = np.frombuffer(result_data, dtype=np.float32).reshape((N, L))
            print(f"[INFO] Результат отримано. Розмір результату: {result.shape}")

            # Вивід частини результату
            print("Фрагмент результату множення:")
            print(result[:5, :5])  # Вивести частину матриці для перевірки

    except Exception as e:
        print(f"[ERROR] Виникла помилка: {e}")

if __name__ == "__main__":
    main()
