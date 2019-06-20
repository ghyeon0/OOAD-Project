from BookControl import BookControl
import os


class BookControlUI:
    def __init__(self):
        self.book_control = BookControl()

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 현재 상태 보기")
        print("2: 책 분실 등록 / 해제")
        print("3: 책 파손 등록 / 해제")
        num = int(input("숫자를 입력하세요: "))
        if num == 1:
            self.show_current_status()
        elif num == 2:
            self.set_missing_status()
        elif num == 3:
            self.set_damaged_status()
        else:
            print("에러")
        input("엔터를 입력하세요.")

    def show_current_status(self, name_only=False):
        os.system('cls' if os.name == 'nt' else 'clear')
        status = self.book_control.get_current_status()
        print("제목\t위치\t작가\t분실\t파손")
        if name_only:
            for i, book in enumerate(status):
                print(str(i + 1) + ":", book.get_title())
        else:
            for book in status:
                print("{}\t{}\t{}\t{}\t{}".format(book.get_title(), book.get_location(), book.get_writer(), book.get_is_missing(), book.get_is_damaged()))
        input("엔터를 입력하세요.")

    def set_missing_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_current_status(name_only=True)
        title = int(input("책 번호를 선택하세요: "))
        value = input("분실 여부 True / False: ")
        self.book_control.set_missing(title, value)
        input("엔터를 입력하세요.")

    def set_damaged_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        title = input("제목을 입력하세요: ")
        value = input("파손 여부 True / False: ")
        self.book_control.set_damaged(title, value)
        input("엔터를 입력하세요.")

    def shutdown(self):
        self.book_control.shutdown()