import socket
import struct

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            for _ in range(100):  # Обробляємо 100 повідомлень
                # Отримуємо заголовок (4 байти, що містять довжину повідомлення)
                header = conn.recv(4)
                if not header:
                    break

                message_length = struct.unpack('!I', header)[0]  # Декодуємо довжину
                data = conn.recv(message_length)  # Отримуємо основне повідомлення
                print(f"Received ({message_length} bytes): {data.decode()}")

                # Відправляємо відповідь
                response = f"Server received: {data.decode()}"
                response_bytes = response.encode()
                response_length = len(response_bytes)
                conn.sendall(struct.pack('!I', response_length))  # Відправляємо заголовок
                conn.sendall(response_bytes)  # Відправляємо основне повідомлення

if __name__ == "__main__":
    start_server()
