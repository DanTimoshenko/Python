def calculate_letter_percentage(filename):
    total_letters = 0
    uppercase_letters = 0
    lowercase_letters = 0

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    total_letters += 1
                    if char.isupper():
                        uppercase_letters += 1
                    else:
                        lowercase_letters += 1

    if total_letters == 0:
        print('The file contains no letters. ')
        return

    uppercase_percentage = (uppercase_letters / total_letters) * 100
    lowercase_percentage = (lowercase_letters / total_letters) * 100

    print('Percentage of capital letters:', uppercase_percentage)
    print('Percentage of lowercase letters:', lowercase_percentage)


calculate_letter_percentage('6.9.txt')

