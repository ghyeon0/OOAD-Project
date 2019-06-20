class Food:
    def __init__(self, name, type, charge):
        self.name = name
        self.type = type
        self.charge = charge

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_charge(self):
        return self.charge

    def set_charge(self, charge):
        self.charge = charge