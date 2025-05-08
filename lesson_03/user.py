class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        print(self.first_name)

    def get_lastname(self):
        print(self.last_name)

    def get_fullname(self):
        print(f"Имя: {self.first_name}, Фамилия: {self.last_name}")
