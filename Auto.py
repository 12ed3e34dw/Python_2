
class Auto:
    #Храние данных
    def __init__(self, Name_Auto="", Models_Auto="", Release_data_Auto="", Creator_Auto="", Engine_volume_Auto="", Color_Auto="", Price_Auto=""):
        self.Name_Auto = Name_Auto
        self.Models_Auto = Models_Auto
        self.Release_data_Auto = Release_data_Auto
        self.Creator_Auto = Creator_Auto
        self.Engine_volume_Auto = Engine_volume_Auto
        self.Color_Auto = Color_Auto
        self.Price_Auto = Price_Auto
    #Получение данных от пользователя
    def input_info_Auto(self):
        print("____________________________________")
        self.Name_Auto = input("Введіть назву машини: ")
        self.Models_Auto = input("Введіть модель машини: ")
        self.Release_data_Auto = input("Введіть рік випуску машини: ")
        self.Creator_Auto = input("Введіть ПІБ виробника: ")
        self.Engine_volume_Auto = input("Введіть об'єм двигуна: ")
        self.Color_Auto = input("Введіть колір машини: ")
        self.Price_Auto = input("Введіть ціну машини: ")
        print("____________________________________")

    #Перезагрузка
    def __eq__(self, new_self):
        if not isinstance(new_self, Auto):
            return NotImplemented
        return (
            self.Name_Auto == new_self.Name_Auto
            and
            self.Models_Auto == new_self.Models_Auto
            and
            self.Release_data_Auto == new_self.Release_data_Auto
            and
            self.Creator_Auto == new_self.Creator_Auto
            and
            self.Engine_volume_Auto == new_self.Engine_volume_Auto
            and
            self.Color_Auto == new_self.Color_Auto
            and
            self.Price_Auto == new_self.Price_Auto
        )
    #Сортировка
    def __lt__(self, new_self):
        if not isinstance(new_self, Auto):
            return NotImplemented
        return self.Release_data_Auto < new_self.Release_data_Auto


    #Присоединение информацию до перезагрузки и после
    def __add__(self, new_self):
        if not isinstance(new_self, Auto):
            return NotImplemented
        return Auto(
            Name_Auto=f"{self.Name_Auto} and {new_self.Name_Auto}",
            Models_Auto=f"{self.Models_Auto} and {new_self.Models_Auto}",
            Release_data_Auto=f"{self.Release_data_Auto} and {new_self.Release_data_Auto}",
            Creator_Auto=f"{self.Creator_Auto} and {new_self.Creator_Auto}",
            Engine_volume_Auto=f"{self.Engine_volume_Auto} and {new_self.Engine_volume_Auto}",
            Color_Auto=f"{self.Color_Auto} and {new_self.Color_Auto}",
            Price_Auto=f"{self.Price_Auto} and {new_self.Price_Auto}",
        )
    #Вывод информации
    def __str__(self):
        return (
            f"____________________________________"
            f"Назва машини: {self.Name_Auto}"
            f"Модель машини: {self.Models_Auto}"
            f"Рік випуску машини: {self.Release_data_Auto}"
            f"ПІБ виробника: {self.Creator_Auto}n"
            f"Об'єм двигуна: {self.Engine_volume_Auto}"
            f"Колір машини: {self.Color_Auto}"
            f"Ціна машини: {self.Price_Auto}"
            f"____________________________________"
        )


# Вывод информации
auto = Auto()
auto.input_info_Auto()
print(auto)
