class Book:
    def __init__(self, Name_Book="",Release_data_Book="",publisher_Book="",Genre_Book="",Author_Book="",Price_Book=""):
      self.Name_Book = Name_Book
      self.Release_data_Book = Release_data_Book
      self.publisher_Book = publisher_Book
      self.Genre_Book = Genre_Book
      self.Author_Book = Author_Book
      self.Price_Book = Price_Book

    def input_info_Book(self):
     print("____________________________________")
     self.Name_Book=input("Введіть назву книги:")
     self.Release_data_Book=input("Введіть рік видання:")
     self.publisher_Book=input("Введіть інформацію про видавця:")
     self.Genre_Book=input("Введіть жанр:")
     self.Author_Book=input("Введіть інформацію про автора книги:")
     self.Price_Book=input("Введіть ціну:")
     print("____________________________________")

    def __str__(self):
        return (
            f"Назва книги: {self.Name_Book}"
            f"Рік видання книги: {self.Release_data_Book}"
            f"Видавець книги: {self.publisher_Book}"
            f"Жанр: {self.Genre_Book}"
            f"Автор: {self.Author_Book}"
            f"Ціна: {self.Price_Book}"

        )
book=Book
book.input_info_Book()
print(book)
