from Book import Book
import csv


class BookControl:
    def __init__(self):
        self.books = []
        self.get_book_data()
        self.max_id = len(self.books)

    def get_current_status(self):
        return self.books

    def get_book_data(self):
        book_info_file = open("./data/book_information.csv")
        book_info = csv.reader(book_info_file)
        for book in list(book_info)[1:]:
            book[0] = int(book[0])
            book[4] = False if book[4] == "False" else True
            book[5] = False if book[5] == "False" else True
            self.books.append(Book(book[0], book[1], book[2], book[3], book[4], book[5]))
        book_info_file.close()

    def shutdown(self):
        book_info_file = open("./data/book_information.csv", 'w', newline='')
        book_writer = csv.writer(book_info_file)
        book_writer.writerow(["id", "title", "location", "writer", "is_missing", "is_damaged"])
        for i, book in enumerate(self.books):
            book_writer.writerow([str(i + 1), str(book.get_title()), str(book.get_location()),
                                  str(book.get_writer()), str(book.get_is_missing()), str(book.get_is_damaged())])
        book_info_file.close()

    def save(self):
        book_info_file = open("./data/book_information.csv", 'w', newline='')
        book_writer = csv.writer(book_info_file)
        book_writer.writerow(["id", "title", "location", "writer", "is_missing", "is_damaged"])
        for i, book in enumerate(self.books):
            book_writer.writerow([str(i + 1), str(book.get_title()), str(book.get_location()),
                                  str(book.get_writer()), str(book.get_is_missing()), str(book.get_is_damaged())])
        book_info_file.close()

    def search_book(self, title):
        books = []
        for book in self.books:
            if title in book.get_title():
                books.append(book)
        if len(books) == 0:
            return -1
        else:
            return books

    def add_new_book(self, title, location, writer):
        new_book = Book(self.max_id + 1, title, location, writer, False, False)
        self.books.append(new_book)
        self.max_id += 1
        self.save()
        self.get_book_data()

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                break

    def set_damaged(self, num, value):
        book = self.books[num - 1]
        if value == "True":
            book.set_is_damaged(True)
        else:
            book.set_is_damaged(False)

    def set_missing(self, num, value):
        book = self.books[num - 1]
        if value == "True":
            book.set_is_missing(True)
        else:
            book.set_is_missing(False)


if __name__ == "__main__":
    c = BookControl()
    for each in c.books:
        print(each.get_title())
    c.remove_book("TEST")
    c.shutdown()
