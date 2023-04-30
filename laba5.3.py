def sqrt(x):

    xn = x / 2.0
    diff = xn ** 2 - x
    count = 0

    while abs(diff) > 1e-4:
        xn = (xn + x / xn) / 2.0
        diff = xn ** 2 - x
        count += 1

    return xn



print(sqrt(5))
print(sqrt(20))
print(sqrt(36))
