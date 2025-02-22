def count_book_words(book_text):
    word_count = len(book_text.split())
    return f"{word_count} words found in the document"

def count_book_letters(book_text):
    book_letters = {}
    letters = book_text.lower()
    for letter in letters:
        book_letters[letter] = book_letters.get(letter, 0) + 1
#        if book_letters.get(letter) == None:
#            book_letters[letter] = 1
#        else:
#           book_letters[letter] += 1
    return book_letters
