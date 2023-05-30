with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

total = sum(numbers)

print(f'Sum of numbers: {total}')

with open('numbers_sum.txt.txt', 'w') as f:
    f.write(str(total))
