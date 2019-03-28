from flask import render_template, Flask, request, url_for, redirect


from app.ozon import create_book, add_book, search_book_by_title, search_book_by_id, remove_book_by_id, \
    create_empty_book, modify_book


def main():
    app = Flask(__name__)

    container = []
    wp = create_book('War and Peace', 'Tolstoy')
    anna = create_book('Anna Karenina', 'Tolstoy')

    container = add_book(container, wp)
    container = add_book(container, anna)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            results = search_book_by_title(container, search)
            return render_template('i.html', books=results, search=search)

        return render_template('i.html', books=container)


    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()

            return redirect(url_for('index'))
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/save', methods=['GET', 'POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        if book_id == 'new':
            book = create_book(title=title, author=author)
            container = add_book(container, book)
            return redirect(url_for('book_details', book_id=book['id']))
        else:
            book = search_book_by_id(container, book_id)
            pass
        return redirect(url_for('book_details', book_id=book['id']))


    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    @app.route('/books/<book_id>/modify', methods=['GET', 'POST'])
    def book_modify(book_id):
        nonlocal container
        book_title = request.form['title']
        book_author = request.form['author']
        container = modify_book(container, book_id, book_title, book_author)
        return redirect(url_for('index'))



    app.run(port=9843, debug=True)

if __name__ == '__main__':
    main()