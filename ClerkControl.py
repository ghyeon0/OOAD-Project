from Clerk import Clerk
from Manager import Manager
import csv
import hashlib


class ClerkControl:
    def __init__(self):
        self.clerks = []
        self.managers = []
        self.get_clerk_data()
        self.get_manager_data()

    def get_clerks(self):
        return self.clerks

    def get_managers(self):
        return self.managers

    def get_clerk_data(self):
        clerk_file = open("./data/clerks.csv")
        clerk_reader = csv.reader(clerk_file)
        for clerk in list(clerk_reader)[1:]:
            self.clerks.append(Clerk(clerk[0], clerk[1]))

    def get_manager_data(self):
        manager_file = open("./data/managers.csv")
        manager_reader = csv.reader(manager_file)
        for manager in list(manager_reader)[1:]:
            self.managers.append(Manager(manager[0], manager[1]))

    def shutdown(self):
        clerk_file = open("./data/clerks.csv", 'w', newline='')
        clerk_writer = csv.writer(clerk_file)
        clerk_writer.writerow(["id", "name"])
        manager_file = open("./data/managers.csv", 'w', newline='')
        manager_writer = csv.writer(manager_file)
        manager_writer.writerow(["id", "name"])
        for clerk in self.clerks:
            clerk_writer.writerow([clerk.get_id(), clerk.get_name()])
        for manager in self.managers:
            manager_writer.writerow([manager.get_id(), manager.get_name()])
            
        clerk_file.close()
        manager_file.close()

    def add_new_clerk(self, name):
        encoded_name = name.encode()
        id = hashlib.sha256(encoded_name).hexdigest()
        new_clerk = Clerk(id, name)
        self.clerks.append(new_clerk)

    def add_new_manager(self, name):
        encoded_name = name.encode()
        id = hashlib.sha256(encoded_name).hexdigest()
        new_manager = Manager(id, name)
        self.managers.append(new_manager)

    def remove_clerk(self, name):
        for clerk in self.clerks:
            if clerk.get_name() == name:
                self.clerks.remove(clerk)
                break

    def remove_manager(self, name):
        for manager in self.managers:
            if manager.get_name() == name:
                self.managers.remove(manager)
                break


if __name__ == "__main__":
    c = ClerkControl()
    c.remove_manager("Dochi")
    c.shutdown()