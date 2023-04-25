import math
i = 2
sum = 0
while i < 16:
    an = (i ** math.log(i)) / (math.log(i)* * i)
    sum += an
    i = i+1

print(sum)