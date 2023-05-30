filename = 'learning_python.txt'

with open(filename, 'r') as file:
    for line in file:
        modified_line = line.replace('Python ', 'C ')
        print(modified_line.strip())

