n = int(input("Введите целое число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Количество цифр в числе:", count)
