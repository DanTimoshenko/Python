n = int(input('Введіть ціле число: '))
count = 0
while n > 0:
    count += 1
    n //= 10
print('Кількість цифр у числі:', count)
