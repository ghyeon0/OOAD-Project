from FoodManagement import FoodManagement
import os


class FoodManagementUI:
    def __init__(self):
        self.food_management = FoodManagement()

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 현재 상태 보기")
        print("2: 음식 추가")
        print("3: 음식 삭제")
        num = int(input("번호 입력: "))
        if num == 1:
            self.show_current_status()
        elif num == 2:
            self.add_new_food()
        elif num == 3:
            self.remove_food()
        input("엔터를 입력하세요.")

    def show_current_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        foods = self.food_management.get_foods()
        for food in foods:
            print("{}\t{}\t{}".format(food.get_name(), food.get_type(), food.get_charge()))
        input("엔터를 입력하세요.")

    def add_new_food(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("음식 이름: ")
        type = input("drink / food: ")
        charge = int(input("가격: "))
        self.food_management.add_new_food(name, type, charge)
        input("엔터를 입력하세요.")

    def remove_food(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("음식 이름: ")
        self.food_management.remove_food(name)
        input("엔터를 입력하세요.")

    def shutdown(self):
        self.food_management.shutdown()