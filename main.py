from stats import count_book_words
from stats import count_book_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = count_book_words(book_text)
    letter_count = count_book_letters(book_text)
    print(letter_count)
    print(word_count)

main()
