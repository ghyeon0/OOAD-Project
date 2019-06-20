from CashPayment import CashPayment
from CardPayment import CardPayment


class OrderControl:
    def __init__(self, food_management, seat_management):
        self.food_management = food_management.food_management
        self.seat_management = seat_management.seat_management

    def make_new_order(self, food_idx, seat_idx):
        charge = self.food_management.get_foods()[food_idx - 1].get_charge()
        self.seat_management.get_seats()[seat_idx - 1].add_amount(charge)

    def pay(self, method, amount, args):
        if method == "CASH":
            payment = CashPayment(amount, args[0])
            if len(args) > 1:
                payment.set_phone_number(args[1])
        else:
            payment = CardPayment(amount, args[0])

        return payment.pay()


