class Book:
    text = True
    page_material = 'бумага'

    def __init__(self, title, author, number_of_pages, isbn, meaning="не зарезервирована"):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.meaning = meaning


class TextBooks(Book):
    def __init__(self, title, author, number_of_pages, isbn, lesson,
                 group, availability_of_tasks, meaning="не зарезервирована"
                 ):
        super().__init__(title, author, number_of_pages, isbn, meaning)
        self.group = group
        self.lesson = lesson
        self.availability_of_tasks = availability_of_tasks


text_books_1 = TextBooks('Алгебра', 'Иванов',
                         200, '12000444',
                         'Математика', 9,
                         True, meaning="зарезервирована"
                         )

text_books_2 = TextBooks('Физика', 'Петров',
                         10, '12000444',
                         'Физика', 7, True
                         )

text_books_3 = TextBooks('Окружающий Мир', 'Иванов',
                         200, '12000444',
                         'Биология', 4, True
                         )

book_1 = Book('Идиот', 'Достоевский', 500, 5423432432,
              meaning="зарезервирована"
              )
book_2 = Book('Война и мир', 'Толстой', 100500, 5423432432)
book_3 = Book('Герой нашего времени', 'Лермонтов', 777, 5423432432)
book_4 = Book('Мертвые души', 'Горький', 20, 5423432432)
book_5 = Book('Горе от ума', 'Грибоедов', 299, 5423432432)


def generation_book(text):
    if text.meaning == "зарезервирована":
        print(f'Название: {text.title}, Автор: {text.author}, '
              f'страниц: {text.number_of_pages}, '
              f'материал: {text.page_material}, {text.meaning}'
              )

    else:
        print(f'Название: {text.title}, Автор: {text.author}, '
              f'страниц: {text.number_of_pages}, '
              f'материал: {text.page_material}'
              )


def generation_text(text):
    if text.meaning == "зарезервирована":
        print(f'Название: {text.title}, Автор: {text.author}, '
              f'страниц: {text.number_of_pages}, '
              f'предмет: {text.lesson}, класс : {text.group}, {text.meaning}'
              )

    else:
        print(f'Название: {text.title}, Автор: {text.author}, '
              f'страниц: {text.number_of_pages}, '
              f'предмет: {text.lesson}, класс : {text.group}'
              )


generation_book(book_1)
generation_book(book_2)
generation_book(book_3)
generation_book(book_4)
generation_book(book_5)

generation_text(text_books_1)
generation_text(text_books_2)
generation_text(text_books_3)
