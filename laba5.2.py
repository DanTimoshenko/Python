num = int(input('Enter an integer'))
if num == 0:
    print('The number of digits is 1')
elif num > 0:
    count = 0
    while num:
        count += 1
        num //= 10
    print('The number of digits in a number', count)
else:
    count = -1
    while num:
        count += 1
        num //= -10
    print('The number of digits in a number', count)
