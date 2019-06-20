from Customer import Customer
import csv


class CustomerControl:
    def __init__(self):
        self.customers = []
        self.get_customer_data()
        self.max_id = len(self.customers)

    def get_customer_data(self):
        customer_file = open("./data/customers.csv")
        customer_reader = csv.reader(customer_file)
        for customer in list(customer_reader)[1:]:
            self.customers.append(Customer(int(customer[0]), customer[1], customer[2], int(customer[3])))
        customer_file.close()

    def shutdown(self):
        customer_file = open("./data/customers.csv", 'w', newline='')
        customer_reader = csv.writer(customer_file)
        customer_reader.writerow(["id", "name", "phone_number", "visit_count"])
        for i, customer in enumerate(self.customers):
            customer_reader.writerow([str(i + 1), customer.get_name(),
                                      customer.get_phone_number(), str(customer.get_visit_count())])
        customer_file.close()

    def add_new_customer(self, name, phone_number):
        self.max_id += 1
        new_customer = Customer(self.max_id, name, phone_number)
        self.customers.append(new_customer)

    def remove_customer(self, phone_number):
        for customer in self.customers:
            if customer.get_phone_number() == phone_number:
                self.customers.remove(customer)
                break

    def search_customer(self, phone_number):
        for customer in self.customers:
            if customer.get_phone_number() == phone_number:
                return customer
        return -1


if __name__ == "__main__":
    c = CustomerControl()
    c.shutdown()


