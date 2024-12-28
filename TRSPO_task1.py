import threading
import time

# Функція для обчислення суми чисел від 1 до 10
def calculate_sum():
    total_sum = 0
    for i in range(1, 11):
        total_sum += i
        time.sleep(0.1)  # Затримка для демонстрації паралельності
    print(f"Сума чисел від 1 до 10: {total_sum}")

# Функція для обчислення добутку чисел від 1 до 5
def calculate_product():
    total_product = 1
    for i in range(1, 6):
        total_product *= i
        time.sleep(0.1)  # Затримка для демонстрації паралельності
    print(f"Добуток чисел від 1 до 5: {total_product}")

# Створюємо два потоки
thread1 = threading.Thread(target=calculate_sum)
thread2 = threading.Thread(target=calculate_product)

# Запускаємо потоки
thread1.start()
thread2.start()

# Чекаємо завершення обох потоків
thread1.join()
thread2.join()

print("Обидва потоки завершили виконання.")
