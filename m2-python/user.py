import datetime


class User:

    def __init__(self, id, nif, birthday, email, phone, password):
        self.id = id
        self.nif = nif
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.password = password


user1 = User(1, "A000001A", datetime.date(1990, 2, 25),
             "user1@pythopn.es", "6416413221", "user1")
user2 = User(2, 'B00002B', datetime.date(1995, 7, 9),
             'user2@python.es', '641145234', 'user2')

print(user1.email, user2.email)
print(user2.nif, user2.nif)

author1 = Author('author1', 2005)

# Añadir libros de uno en uno
# author1.books.append(book1)
# author1.books.append(book2)

# Añadir varios libros a la vez
author1.books = author1.books + [book1, book2]

print("fin")
# # Clase Author
# class Author:
#     def __init__(self, name, year, books):
#         self.name = name
#         self.year = year
#         self.books = books # Asociación de a muchos (Many)

# book1 = Book('book1', 350)
# book2 = Book('book2', 437)

# books = [book1, book2]
# author1 = Author('author1', 2005, books)
