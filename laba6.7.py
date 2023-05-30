def format_text(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            formatted_text = text.replace('\n', ' ')

        with open('formatted_text.txt', 'w') as file:
            file.write(formatted_text)

        print('The text was successfully formatted and written to the file "formatted_text.txt ".')

    except FileNotFoundError:
        print('file not found')


format_text('laba6.7.txt')
