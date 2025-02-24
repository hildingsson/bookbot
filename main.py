from stats import count_book_words
from stats import count_book_letters
from stats import sorted_list
import sys

def get_book_text(file_path):
    try:
      with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    except FileNotFoundError:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_book_words(book_text)
    letter_count = count_book_letters(book_text)
    new_list = sorted_list(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in new_list:
        for key, value in item.items():
            print(f"{key}: {value}")
    print("============= END ===============")
main()