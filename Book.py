class Book:
    # Храние данных
    def __init__(self, Name_Book="",Release_data_Book="",publisher_Book="",Genre_Book="",Author_Book="",Price_Book=""):
      self.Name_Book = Name_Book
      self.Release_data_Book = Release_data_Book
      self.publisher_Book = publisher_Book
      self.Genre_Book = Genre_Book
      self.Author_Book = Author_Book
      self.Price_Book = Price_Book

    # Получение данных от пользователя
    def input_info_Book(self):
     print("____________________________________")
     self.Name_Book=input("Введіть назву книги:")
     self.Release_data_Book=input("Введіть рік видання:")
     self.publisher_Book=input("Введіть інформацію про видавця:")
     self.Genre_Book=input("Введіть жанр:")
     self.Author_Book=input("Введіть інформацію про автора книги:")
     self.Price_Book=input("Введіть ціну:")
     print("____________________________________")
    # Перезагрузка
    def __eq__(self, new_self):
        if not isinstance(new_self, Book):
            return NotImplemented
        return (
          self.Name_Book == new_self.Name_Book
           and
          self.Release_data_Book == new_self.Release_data_Book
           and
          self.publisher_Book == new_self.publisher_Book
           and
          self.Genre_Book == new_self.Genre_Book
           and
          self.Author_Book == new_self.Author_Book
           and
          self.Price_Book == new_self.Price_Book

        )
    # Сортировка
    def __lt__(self, new_self):
        if not isinstance(new_self, Book):
            return NotImplemented
       return self.Release_data_Book < new_self.Release_data_Book
    # Присоединение информацию до перезагрузки и после
    def __add__(self, new_self):
        if not isinstance(new_self, Book):
            return NotImplemented
        return Book(
              Name_Book=f"{self.Name_Book} and {new_self.Name_Book}",
              Release_data_Book= f"{self.Release_data_Book} and {new_self.Release_data_Book}",
              publisher_Book= f"{self.publisher_Book} and {new_self.publisher_Book}",
              Genre_Book= f"{self.Genre_Book} and {new_self.Genre_Book}",
              Author_Book= f"{self.Author_Book} and {new_self.Author_Book}",
              Price_Book= f"{self.Price_Book} and {new_self.Price_Book}",
        )
 
    def __str__(self):
        return (
            f"Назва книги: {self.Name_Book}"
            f"Рік видання книги: {self.Release_data_Book}"
            f"Видавець книги: {self.publisher_Book}"
            f"Жанр: {self.Genre_Book}"
            f"Автор: {self.Author_Book}"
            f"Ціна: {self.Price_Book}"
        )
# Вывод информации
book=Book
book.input_info_Book()
print(book)
