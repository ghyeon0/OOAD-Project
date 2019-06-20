from OrderControl import OrderControl
import os


class OrderControlUI:
    def __init__(self, food_management, seat_management):
        self.order_control = OrderControl(food_management, seat_management)

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 주문하기")
        print("2: 결제하기")
        num = int(input("번호 입력: "))
        if num == 1:
            self.make_new_order()
        elif num == 2:
            self.pay(input("CARD / CASH? "))

    def make_new_order(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        foods = self.order_control.food_management.get_foods()
        for i, food in enumerate(foods):
            print("{}:\t{}\t{}\t{}".format(str(i + 1), food.get_name(), food.get_type(), food.get_charge()))
        food_idx = int(input("음식 번호 선택: "))
        seat_idx = int(input("좌석 번호 입력: "))
        self.order_control.make_new_order(food_idx, seat_idx)
        input("엔터를 입력하세요.")

    def pay(self, method):
        os.system('cls' if os.name == 'nt' else 'clear')
        seat_idx = int(input("좌석 번호 입력: "))
        amount = self.order_control.seat_management.get_seats()[seat_idx - 1].get_total_amount()
        if method == "CASH":
            received = int(input("받은 돈: "))
            num = int(input("현금 영수증 발급 1 / 미발급 0"))
            if num == 1:
                phone_number = input("핸드폰 번호 입력: ")
                lst = [received, phone_number]
            else:
                lst = [received]

        else:
            card_number = input("카드 번호 입력: ")
            lst = [card_number]
        result = self.order_control.pay(method, amount, lst)
        if result:
            seat = self.order_control.seat_management.get_seats()[seat_idx - 1]
            seat.set_is_empty(True)
            seat.set_plan(None)
            seat.set_start_time(None)
            seat.set_total_amount(0)
        else:
            print("에러")
        input("엔터를 입력하세요.")