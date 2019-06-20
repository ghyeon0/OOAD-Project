from CustomerControl import CustomerControl
import os


class CustomerControlUI:
    def __init__(self):
        self.customer_control = CustomerControl()

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 고객 추가")
        print("2: 고객 삭제")
        num = int(input("번호 입력: "))
        if num == 1:
            self.add_new_customer()
        elif num == 2:
            self.remove_customer()

    def add_new_customer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("이름 입력: ")
        phone_number = input("휴대폰 번호 입력: ")
        self.customer_control.add_new_customer(name, phone_number)
        input("엔터를 입력하세요.")

    def remove_customer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        phone_number = input("휴대폰 번호 입력: ")
        self.customer_control.remove_customer(phone_number)
        input("엔터를 입력하세요.")

    def shutdown(self):
        self.customer_control.shutdown()
