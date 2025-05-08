class Address:
    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return f"город: {self.city}, индекс: {self.index}, улица: {self.street}, дом: {self.building} - {self.apartment}"


