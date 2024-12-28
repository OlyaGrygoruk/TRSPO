import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Функція для обчислення кількості кроків до виродження в 1
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

if __name__ == "__main__":
    # Генеруємо 10 мільйонів випадкових натуральних чисел
    numbers = [random.randint(1, 100000) for _ in range(100000)]

    # Кількість потоків
    num_threads = 8

    # Атомарні змінні для підрахунку
    total_steps = 0  # Загальна кількість кроків
    count = 0  # Кількість обчислених чисел

    # Лок для синхронізації доступу до змінних
    lock = Lock()

    def safe_increment(total, increment, is_count=False):
        """Функція для безпечного оновлення значень."""
        global total_steps, count
        with lock:
            if is_count:
                count += increment
            else:
                total_steps += increment

    # Виконуємо паралельне обчислення за допомогою ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(collatz_steps, number) for number in numbers]

        for future in as_completed(futures):
            steps = future.result()
            safe_increment(total_steps, steps)
            safe_increment(count, 1, is_count=True)

    # Підраховуємо середню кількість кроків
    average_steps = total_steps / count if count > 0 else 0

    print(f"Середня кількість кроків для виродження в 1: {average_steps}")
