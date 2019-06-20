class Book:
    def __init__(self, id, title, location, writer, is_missing, is_damaged):
        self.id = id
        self.title = title
        self.location = location
        self.writer = writer
        self.is_missing = is_missing
        self.is_damaged = is_damaged

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_name(self, title):
        self.title = title

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_writer(self):
        return self.writer

    def set_writer(self, writer):
        self.writer = writer

    def get_is_missing(self):
        return self.is_missing

    def set_is_missing(self, is_missing):
        self.is_missing = is_missing

    def get_is_damaged(self):
        return self.is_damaged

    def set_is_damaged(self, is_damaged):
        self.is_damaged = is_damaged



