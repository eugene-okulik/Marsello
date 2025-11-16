class Book:
    text = True
    page_material = 'бумага'

    def __init__(self, title, author, number_of_pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def generation_book(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.number_of_pages}, '
                  f'материал: {self.page_material}, зарезервирована'
                  )

        else:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.number_of_pages}, '
                  f'материал: {self.page_material}'
                  )


class TextBooks(Book):
    def __init__(self, title, author, number_of_pages, isbn, lesson,
                 group, availability_of_tasks, reserved=False
                 ):
        super().__init__(title, author, number_of_pages, isbn, reserved)
        self.group = group
        self.lesson = lesson
        self.availability_of_tasks = availability_of_tasks

    def generation_text(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.number_of_pages}, '
                  f'предмет: {self.lesson}, класс : {self.group}, зарезервирована'
                  )

        else:
            print(f'Название: {self.title}, Автор: {self.author}, '
                  f'страниц: {self.number_of_pages}, '
                  f'предмет: {self.lesson}, класс : {self.group}'
                  )


text_books = [
    TextBooks('Алгебра', 'Иванов', 200, '12000444',
              'Математика', 9, True
              ),

    TextBooks('Физика', 'Петров', 10,
              '12000444', 'Физика', 7, True
              ),

    TextBooks('Окружающий Мир', 'Иванов', 200,
              '12000444', 'Биология', 4, True
              )
]

books = [
    Book('Идиот', 'Достоевский', 500, 5423432432),
    Book('Война и мир', 'Толстой', 100500, 5423432432),
    Book('Герой нашего времени', 'Лермонтов', 777, 5423432432),
    Book('Мертвые души', 'Горький', 20, 5423432432),
    Book('Горе от ума', 'Грибоедов', 299, 5423432432),
]

books[0].reserved = True
text_books[0].reserved = True

for book in books:
    book.generation_book()

for text in text_books:
    text.generation_text()
