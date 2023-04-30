def sqrt(x):

    xn = x / 2.0
    diff = xn ** 2 - x
    count = 0

    while abs(diff) > 1e-4:
        xn = (xn + x / xn) / 2.0
        diff = xn ** 2 - x
        count += 1

    print(f"Вычисление квадратного корня {x} методом Герона заняло {count} итераций.")
    return xn


# Пример использования функции sqrt
print(sqrt(5))
print(sqrt(20))
print(sqrt(36))