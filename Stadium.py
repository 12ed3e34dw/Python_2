class Stadium:
    # Хранение данных
    def __init__(self, Name_Stadium="", Opening_date_Stadium="", Country="", City="", Capacity_Stadium=""):
        self.Name_Stadium = Name_Stadium
        self.Opening_date_Stadium = Opening_date_Stadium
        self.Country = Country
        self.City = City
        self.Capacity_Stadium = Capacity_Stadium

    # Получение данных от пользователя
    def input_info_Stadium(self):
        print(" _____________________________________________")
        self.Name_Stadium = input("Введіть назву стадіона: ")
        self.Opening_date_Stadium = input("Введіть дату відкриття стадіона: ")
        self.Country = input("Введіть країну: ")
        self.City = input("Введіть місто: ")
        self.Capacity_Stadium = input("Введіть місткість стадіона: ")
        print(" _____________________________________________")

    # Перезагрузка для сравнения 
    def __eq__(self, new_self):
        if not isinstance(new_self, Stadium):
            return NotImplemented
        return (
            self.Name_Stadium == new_self.Name_Stadium
            and self.Opening_date_Stadium == new_self.Opening_date_Stadium
            and self.Country == new_self.Country
            and self.City == new_self.City
            and self.Capacity_Stadium == new_self.Capacity_Stadium
        )

    # Сортировка
    def __lt__(self, new_self):
        if not isinstance(new_self, Stadium):
            return NotImplemented
        return self.Opening_date_Stadium < new_self.Opening_date_Stadium

    # Присоединение информации
    def __add__(self, new_self):
        if not isinstance(new_self, Stadium):
            return NotImplemented
        return Stadium(
            Name_Stadium=f"{self.Name_Stadium} and {new_self.Name_Stadium}",
            Opening_date_Stadium=f"{self.Opening_date_Stadium} and {new_self.Opening_date_Stadium}",
            Country=f"{self.Country} and {new_self.Country}",
            City=f"{self.City} and {new_self.City}",
            Capacity_Stadium=f"{self.Capacity_Stadium} and {new_self.Capacity_Stadium}",
        )

    # Преобразование в строку
    def __str__(self):
        return (
            "_____________________________________________\n"
            f"Название стадіона: {self.Name_Stadium}\n"
            f"Дата відкриття стадіона: {self.Opening_date_Stadium}\n"
            f"Країна: {self.Country}\n"
            f"Місто: {self.City}\n"
            f"Місткість: {self.Capacity_Stadium}\n"
            "_____________________________________________"
        )


# Вывод информации
stadium = Stadium()
stadium.input_info_Stadium()
print(stadium)
