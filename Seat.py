class Seat:
    def __init__(self, id):
        self.id = id
        self.is_empty = True
        self.plan = None
        self.start_time = None
        self.total_amount = 0

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_is_empty(self):
        return self.is_empty

    def set_is_empty(self, is_empty):
        self.is_empty = is_empty

    def get_plan(self):
        return self.plan

    def set_plan(self, plan):
        self.plan = plan

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount

    def add_amount(self, amount):
        self.total_amount += amount