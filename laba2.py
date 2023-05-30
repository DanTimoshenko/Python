# IKM221K lab number 22
# Timoshenko Daniil 18
print('''IKM221K lab number 2
Timoshenko Daniil 18''')

TEMPLATE = 'input please { }: '
x = int(input(TEMPLATE.format('x')))
y = int(input(TEMPLATE.format('y')))
z = int(input(TEMPLATE.format('z')))

a = x - (x + (y / z)) / (78 + y)
print(a)
