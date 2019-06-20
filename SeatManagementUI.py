from SeatManagement import SeatManagement
from datetime import datetime
import os


class SeatManagementUI:
    def __init__(self):
        self.seat_management = SeatManagement()

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1: 현재 좌석 상태 보기")
        print("2: 좌석 선택")
        print("3: 요금제 추가")
        print("4: 요금제 삭제")
        num = int(input("번호 입력: "))
        if num == 1:
            self.show_current_seat_status()
        elif num == 2:
            self.select_seat()
        elif num == 3:
            self.add_new_time_plan()
        elif num == 4:
            self.remove_time_plan()

    def show_current_seat_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        status = self.seat_management.get_seats()
        print("번호\t빈 자리\t요금제\t시작 시간\t\t\t\t결제 금액")
        for i, seat in enumerate(status):
            print("{}\t{}\t{}\t{}\t\t\t\t{}".format(seat.get_id(), seat.get_is_empty(), seat.get_plan(),
                                                    seat.get_start_time(), seat.get_total_amount()))
        input("엔터를 입력하세요.")

    def select_seat(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_current_seat_status()
        idx = int(input("좌석 번호 입력: "))
        self.seat_management.get_seats()[idx - 1].set_is_empty(False)
        self.seat_management.get_seats()[idx - 1].set_start_time(datetime.now())
        time_plans = self.seat_management.get_time_plans()
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, time_plan in enumerate(time_plans):
            print("{}\t{}\t{}\t{}".format(str(i + 1), time_plan.get_id(), time_plan.get_time(), time_plan.get_charge()))
        plan_idx = int(input("요금제 번호 입력: "))
        self.seat_management.get_seats()[idx - 1].set_plan(time_plans[plan_idx - 1].get_id())
        self.seat_management.get_seats()[idx - 1].add_amount(time_plans[plan_idx - 1].get_charge())
        input("엔터를 입력하세요.")

    def add_new_time_plan(self):
        pass

    def remove_time_plan(self):
        pass

    def shutdown(self):
        self.seat_management.shutdown()
