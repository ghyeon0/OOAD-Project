from ClerkControl import ClerkControl
import os


class ClerkControlUI:
    def __init__(self):
        self.clerk_control = ClerkControl()

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 직원 추가")
        print("2: 직원 삭제")
        print("3: 매니저 추가")
        print("4: 매니저 삭제")
        num = int(input("번호 입력: "))
        if num == 1:
            self.add_clerk()
        elif num == 2:
            self.remove_clerk()
        elif num == 3:
            self.add_manager()
        elif num == 4:
            self.remove_manager()

    def add_clerk(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("이름 입력: ")
        self.clerk_control.add_new_clerk(name)
        input("엔터를 입력하세요.")

    def remove_clerk(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("이름 입력: ")
        self.clerk_control.remove_clerk(name)
        input("엔터를 입력하세요.")

    def add_manager(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("이름 입력: ")
        self.clerk_control.add_new_manager(name)
        input("엔터를 입력하세요.")

    def remove_manager(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("이름 입력: ")
        self.clerk_control.remove_manager(name)
        input("엔터를 입력하세요.")

    def shutdown(self):
        self.clerk_control.shutdown()
