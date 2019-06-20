from Clerk import Clerk


class Manager(Clerk):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.is_manager = True
