import math
i = 2
summa = 0
NUMBER_OF_ELEMENTS = 16

while i < NUMBER_OF_ELEMENTS:
    an = (i ** math.log(i)) / (math.log(i) ** i)
    summa += an
    i = i + 1

print(summa)
