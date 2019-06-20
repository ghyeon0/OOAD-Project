class TimePlan:
    def __init__(self, id, time, charge):
        self.id = id
        self.time = time
        self.charge = charge

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_charge(self):
        return self.charge

    def set_charge(self, charge):
        self.charge = charge
