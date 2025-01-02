class Auto:

 def __init__(self,Name_Auto="",Models_Auto="",Release_data_Auto="",Creator_Auto="",Engine_volume_Auto="",Color_Auto="",Price_Auto=""):
  self.Name_Auto=Name_Auto
  self.Models_Auto=Models_Auto
  self.Release_data_Auto=Release_data_Auto
  self.Creator_Auto=Creator_Auto
  self.Engine_volume_Auto=Engine_volume_Auto
  self.Color_Auto=Color_Auto
  self.Price_Auto=Price_Auto


 def input_info_Auto(self):
   print("____________________________________")
   self.Name_Auto=input("Введіть назву машини:")
   self.Models_Auto=input("Введіть модель машини:")
   self.Release_data_Auto=input("Введіть рік випуску машини:")
   self.Creator_Auto=input("Введіть ПІБ виробника:")
   self.Engine_volume_Auto=input("Введіть об'єм двигуна:")
   self.Color_Auto=input("Введіть колір машини:")
   self.Price_Auto=input("Введіть ціну машини:")
   print("____________________________________")

 def __str__(self):
    return (
  f"Назва машини: {self.Name_Auto}\n"
  f"Модель машини: {self.Models_Auto}\n"
  f"Рік випуску машини: {self.Release_data_Auto}\n"
  f"ПІБ виробника: {self.Creator_Auto}\n"
  f"об'єм двигуна: {self.Engine_volume_Auto}\n"
  f"Колір машини: {self.Color_Auto}\n"
  f"Ціна машини: {self.Price_Auto}\n"
         )

auto=Auto()
auto.input_info_Auto()
print(auto)
