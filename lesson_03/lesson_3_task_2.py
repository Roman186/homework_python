from smartphone import Smartphone

catalog = [Smartphone("Xiaomi", "mi 10", "+79825307845"),
           Smartphone("Realme", "Note 8", "+79205307245"),
           Smartphone("Oneplus", "Nord 4", "+79194537840"),
           Smartphone("Samsung", "A 53", "+79194837880"),
           Smartphone("Iphone", "15 pro", "+79224587640")
           ]

for smartphone in catalog:
    print(f"Марка телефона: {smartphone.brand}, Модель: {smartphone.model}, Номер: {smartphone.number}")

