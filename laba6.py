with open('numbers.txt', 'r') as f:
    # Читаємо кожен рядок і конвертуємо його в ціле число
    numbers = [int(line.strip()) for line in f.readlines()]

# Обчислюємо суму чисел
total = sum(numbers)

# Виводимо суму на екран
print(f"Сума чисел: {total}")

# Відкриваємо файл sum_numbers.txt для запису
with open('sum_numbers.txt', 'w') as f:
    # Записуємо суму у файл
    f.write(str(total))