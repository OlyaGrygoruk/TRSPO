import random
from concurrent.futures import ProcessPoolExecutor, as_completed


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
    # Генеруємо мільйон випадкових натуральних чисел
    numbers = [random.randint(1, 100000) for _ in range(100000)]

    # Кількість процесів (така сама, як кількості ядер процесора)
    num_processes = 8

    # Виконуємо паралельне обчислення за допомогою ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(collatz_steps, number) for number in numbers]

        total_steps = 0
        count = 0

        for future in as_completed(futures):
            steps = future.result()
            total_steps += steps
            count += 1

    # Підраховуємо середню кількості кроків
    average_steps = total_steps / count if count > 0 else 0

    print(f"Середня кількість кроків для виродження в 1: {average_steps}")
