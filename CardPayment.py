from Payment import Payment


class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_card_number(self):
        return self.card_number

    def set_card_number(self, card_number):
        self.card_number = card_number

    def pay(self):
        if self.verify_card_number():
            self.print_receipt()
            return True
        else:
            return False

    def verify_card_number(self):
        return True

    def print_receipt(self):
        print(self.card_number)
        print(self.amount)
