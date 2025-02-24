def count_book_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_book_letters(book_text):
    book_letters = {}
    letters = book_text.lower()
    for letter in letters:
        book_letters[letter] = book_letters.get(letter, 0) + 1
    return book_letters

def sorted_list(book_letters):
    test_list = []
    sorted_list = sorted(book_letters.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_list:
        if key.isalpha():
            test_list.append({key: value})
    return test_list