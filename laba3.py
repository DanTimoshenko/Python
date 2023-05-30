# IKM221K lab number 3
# Timoshenko Daniil 18
print('''IKM221K lab number 1
Timoshenko Daniil 18''')
TEMPLATE = 'input please {}: '
x = int(input(TEMPLATE.format('x')))
z = int(input(TEMPLATE.format('z')))

if x < -3 or x > 3:
    a = (abs((x**3) - (z**3))/(((x**2)-9)**1/2))
    print(a)
elif x == 3 or x == -3:
    print('impossible, because divide by zero ')
elif -3 < x < 3:
    print('impossible because the negative root')
