TEMPLATE = 'input please {}: '
number = int(input(TEMPLATE.format('number')))
if number % 2 == 0:
    parity = 'paired'
else:
    parity = 'not paired'


filename = "parity.txt"
with open(filename, "w") as file:
    file.write(f'Number {number} є {parity}.')

print(f'The information is recorded in the file {filename}.')
