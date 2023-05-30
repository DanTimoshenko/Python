filename = 'learning_python.txt'

lines = []

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        lines.append(line)


for line in lines:
    print(line)
