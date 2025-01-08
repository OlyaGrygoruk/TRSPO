# Використовуємо офіційний Python-образ
FROM python:3.11

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо локальні файли в контейнер
COPY . .

# Встановлюємо необхідні залежності (якщо є requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || echo "No dependencies"

# Встановлюємо бібліотеку для дебагу
RUN pip install debugpy

# Запускаємо сервер у режимі дебагу
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "server.py"]

