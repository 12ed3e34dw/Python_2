class Stadium:

 def __init__(self, Name_Stadium="",Opening_date_Stadium="",Country="",City="",Capacity_Stadium=""):
     self.Name_Stadium = Name_Stadium
     self.Opening_date_Stadium = Opening_date_Stadium
     self.Country = Country
     self.City = City
     self.Capacity_Stadium = Capacity_Stadium

 def input_info_Stadium(self):
    print(" _____________________________________________")
    self.Name_Stadium = input("Введіть назву стадіона:")
    self.Opening_date_Stadium = input("Введіть дату відкриття стадіона:")
    self.Country = input("Введіть країну:")
    self.City = input("Введіть город:")
    self.Capacity_Stadium = input("Введіть місткість стадіона:")
    print(" _____________________________________________")

 def __str__(self):
    return (
        f"_____________________________________________"
        f"Название стадіона: {self.Name_Stadium}"
        f"Дата відкриття стадіона: {self.Opening_date_Stadium}"
        f"Країна: {self.Country}"
        f"Місто: {self.City}"
        f"Місткість: {self.Capacity_Stadium}"
        f"_____________________________________________"
    )

stadium=Stadium()
stadium.input_info_Stadium()
print(stadium)
