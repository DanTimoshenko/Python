# IKM221K lab number 4
# Timoshenko Daniil 18
print('''IKM221K lab number 1
Timoshenko Daniil 18''')

n = int(input('Enter the seed number '))
m = int(input('Enter the final number : '))

for i in range(n, m + 1):
    if i % 3 == 0 and i % 2 != 0:
        print(i)
