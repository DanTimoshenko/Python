filename = 'guest_book.txt'


open(filename, 'w').close()

print('Enter guest names (enter "q" to exit):')

while True:
    name = input('Name: ')

    if name == 'q':
        break

    greeting = f'Welcome, {name}!'
    print(greeting)

    with open(filename, 'a') as file:
        file.write(greeting + '\n')

print('The data is stored in a guest_book.txt file')
