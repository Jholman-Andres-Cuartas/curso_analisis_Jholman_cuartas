

# Asociacion

# UNidimencional: solo desde un lado de la asocición podemos acceder al objeto de la otra clase
# Por ejemplo: desde author puedo acceder a un libro, pero desde el libro no puedo acceder al autor
# Bidimencional: desde ambos lados de la asociación podemos acceder a el objeto de la otra clase
# Por ejemplo: desde autor puede acceder a un libro y desde un libro  puedo acceder al autor.

# clase Book

class Book:
    def __init__(self, title, num_pages):
    self.title = title
    self.num_pages = num_pages


# Clase Author

class Author:
    def __init__(self, name, year):
    self.name = name
    self.year = year

book1 = Book('book1', 350)
book2 = Book('book2', 437)
author1 = Author('author1', 2005, books)

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
