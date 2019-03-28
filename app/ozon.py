import uuid

#str(uuid.uuid4()),#

def create_book(title, author):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
    }


def create_empty_book():
    return {
        'id': str(uuid.uuid4()),
        'title': '',
        'author': '',
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_book_by_title(container, title):
    result = []
    for book in container:
        if book['title'] == title:
            result.append(book)
    return result


def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book

def remove_book_by_id(container, book_id):
    result=[]
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result

def modify_book(container, book_id, book_title=None, book_author=None):
    result = []
    for book in container:
        if book_id == book['id']:
            book['title'] = book_title
            book['author'] = book_author
        result.append(book)
    return result

