def count_the_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            text = text.lower()
            sentences = text.split('.')

            for i, sentence in enumerate(sentences):
                count = sentence.count('the')
                print(f'text {i + 1}: Number of occurrences "the ": {count}')

    except FileNotFoundError:
        print("File not found")


count_the_occurrences('book.txt')

