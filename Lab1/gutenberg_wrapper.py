""" Fetches books from the gutenberg project """
import sys
import urllib_wrapper

DEFAULT_BOOK_IDS = [
    59780,
    59802
]

BOOK_URL = BOOK_URL = "https://www.gutenberg.org/files/{0}/{0}-0.txt"


def getBooks(book_ids):
    """ Downloads books and returns a list of their file names """
    if book_ids:
        books = [BOOK_URL.format(item) for item in sys.argv[1:]]
    else:
        books = [BOOK_URL.format(item) for item in DEFAULT_BOOK_IDS]

    file_names = ["book_{}.txt".format(i + 1) for i in range(len(books))]

    for i in range(len(books)):
        file_name = file_names[i]
        book_url = books[i]
        urllib_wrapper.downloadBook(book_url, file_name)

    return file_names
