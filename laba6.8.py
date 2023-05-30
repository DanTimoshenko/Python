import re


def extract_chapter_titles(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            chapter_pattern = r'CHAPTER\s+\w+.\s+.\w+.\w+.\w+.\w+.\w+.\w+.'
            chapters = re.findall(chapter_pattern, text)

        with open('chapter.txt', 'w') as file:
            for chapter in chapters:
                file.write(chapter + '\n')

        print('Section headings have been successfully extracted and written to a file "chapter.txt".')

    except FileNotFoundError:
        print('File not found')


extract_chapter_titles('123.txt')
