from Pos import Pos
import os


class PosUI:
    def __init__(self):
        self.pos = Pos()

    def show(self):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("1: 책 관리 시스템")
                print("2: 자리 관리 시스템")
                print("3: 주문받기 / 결제하기")
                print("4: 직원 관리 시스템")
                print("5: 고객 관리 시스템")
                print("6: 음식 관리 시스템")
                num = int(input("번호를 입력하세요: "))
                if num == 1:
                    self.show_book_control_ui()
                elif num == 2:
                    self.show_seat_management_ui()
                elif num == 3:
                    self.show_order_control_ui()
                elif num == 4:
                    self.show_clerk_control_ui()
                elif num == 5:
                    self.show_customer_control_ui()
                elif num == 6:
                    self.show_food_management_ui()
            except KeyboardInterrupt:
                self.shutdown()
                break

    def show_book_control_ui(self):
        self.pos.book_control_ui.show()

    def show_seat_management_ui(self):
        self.pos.seat_management_ui.show()

    def show_order_control_ui(self):
        self.pos.order_control_ui.show()

    def show_clerk_control_ui(self):
        self.pos.clerk_control_ui.show()

    def show_customer_control_ui(self):
        self.pos.customer_control_ui.show()

    def show_food_management_ui(self):
        self.pos.food_management_ui.show()

    def shutdown(self):
        self.pos.shutdown()


if __name__ == "__main__":
    c = PosUI()
    c.show()