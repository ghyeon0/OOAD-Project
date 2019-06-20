from Seat import Seat
from TimePlan import TimePlan
import csv


class SeatManagement:
    def __init__(self):
        self.seats = []
        self.time_plans = []
        self.get_seat_data()
        self.get_time_plan_data()
        self.max_time_plan_length = len(self.time_plans)

    def get_seats(self):
        return self.seats

    def get_time_plans(self):
        return self.time_plans

    def get_seat_data(self):
        for i in range(10):
            self.seats.append(Seat(i + 1))

    def get_time_plan_data(self):
        time_plan_file = open("./data/time_plan.csv")
        time_plan_reader = csv.reader(time_plan_file)
        for time_plan in list(time_plan_reader)[1:]:
            self.time_plans.append(TimePlan(time_plan[0], int(time_plan[1]), int(time_plan[2])))

        time_plan_file.close()

    def add_new_time_plan(self, time, charge):
        self.max_time_plan_length += 1
        self.time_plans.append(TimePlan(chr(self.max_time_plan_length + 64), time, charge))

    def remove_time_plan(self, time):
        for time_plan in self.time_plans:
            if time_plan.get_time() == time:
                self.time_plans.remove(time_plan)

    def shutdown(self):
        time_plan_file = open("./data/time_plan.csv", 'w', newline='')
        time_plan_writer = csv.writer(time_plan_file)
        time_plan_writer.writerow(["id", "time", "charge"])
        for time_plan in self.time_plans:
            time_plan_writer.writerow([time_plan.get_id(), str(time_plan.get_time()), str(time_plan.get_charge())])
