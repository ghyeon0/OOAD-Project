class Clerk:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.is_manager = False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_is_manager(self):
        return self.is_manager

    def set_is_manager(self, is_manager):
        self.is_manager = is_manager

