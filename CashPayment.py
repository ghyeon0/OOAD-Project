from Payment import Payment


class CashPayment(Payment):
    def __init__(self, amount, received, phone_number="010-0000-0000"):
        super().__init__(amount)
        self.received = received
        self.phone_number = phone_number

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_received(self):
        return self.received

    def set_received(self, received):
        self.received = received

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def pay(self):
        print("Amount:", self.amount)
        print("Received:", self.received)
        print("Change:", self.received - self.amount)
        self.print_cash_receipt()
        return True

    def print_cash_receipt(self):
        print(self.amount)
        print(self.phone_number)
