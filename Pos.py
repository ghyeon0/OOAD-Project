from BookControlUI import BookControlUI
from ClerkControlUI import ClerkControlUI
from CustomerControlUI import CustomerControlUI
from SeatManagementUI import SeatManagementUI
from FoodManagementUI import FoodManagementUI
from OrderControlUI import OrderControlUI


class Pos:
    def __init__(self):
        self.book_control_ui = BookControlUI()
        self.clerk_control_ui = ClerkControlUI()
        self.customer_control_ui = CustomerControlUI()
        self.seat_management_ui = SeatManagementUI()
        self.food_management_ui = FoodManagementUI()
        self.order_control_ui = OrderControlUI(self.food_management_ui, self.seat_management_ui)

    def shutdown(self):
        print()
        print("--------------------------------")
        self.book_control_ui.shutdown()
        print("Book Control System Shutdown")
        self.clerk_control_ui.shutdown()
        print("Clerk Control System Shutdown")
        self.customer_control_ui.shutdown()
        print("Customer Control System Shutdown")
        self.seat_management_ui.shutdown()
        print("Seat Management System Shutdown")
        self.food_management_ui.shutdown()
        print("Food Management System Shutdown")
        print("System Shutdown")