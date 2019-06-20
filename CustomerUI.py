from BookControl import BookControl
import os


class CustomerUI:
    def __init__(self):
        self.book_control = BookControl()

    def show(self):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                name = input("책 제목을 입력하세요: ")
                self.search_book(name)
            except KeyboardInterrupt:
                break

    def search_book(self, name):
        books = self.book_control.search_book(name)
        if books != -1:
            for book in books:
                print("제목:", book.get_title())
                print("위치:", book.get_location())
        else:
            print("책을 찾을 수 없습니다.")
        input("검색하려면 엔터를 입력하세요.")


if __name__ == "__main__":
    customer_ui = CustomerUI()
    customer_ui.show()