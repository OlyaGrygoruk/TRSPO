import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Отримання даних від клієнта
                data = conn.recv(1024)
                if not data:  # Якщо даних немає, з'єднання закрито
                    print("Client disconnected")
                    break

                print(f"Client: {data.decode()}")  # Відображення отриманого повідомлення
                # Відповідь клієнту
                message = input("You (Server): ")
                conn.sendall(message.encode())  # Відправка даних клієнту

if __name__ == "__main__":
    start_server()
