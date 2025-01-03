import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # Відправлення повідомлення серверу
            message = input("You (Client): ")
            if message.lower() == 'exit':  # Завершення з'єднання
                print("Disconnecting from server...")
                break
            client_socket.sendall(message.encode())

            # Отримання відповіді від сервера
            data = client_socket.recv(1024)
            print(f"Server: {data.decode()}")

if __name__ == "__main__":
    start_client()
