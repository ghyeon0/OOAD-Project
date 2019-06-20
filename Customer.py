class Customer:
    def __init__(self, id, name, phone_number, visit_count=0):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.visit_count = visit_count

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_visit_count(self):
        return self.visit_count

    def set_visit_count(self, visit_count):
        self.visit_count = visit_count

    def increase_visit_count(self):
        self.visit_count += 1

    def decrease_visit_count(self):
        self.visit_count -= 1

    def use_coupon(self):
        if self.visit_count >= 10:
            self.visit_count -= 10
            return 0
        else:
            return -1
