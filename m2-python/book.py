# el método __str__ permite que se muestre el texto que queramos cuando se imprime un objeto con print 

# El método __str__ de python es equivalente al método toString() de java
class Book:
    def __init__(self, title, num_pages):
        self.title = title
def __str__(self):


book1 = Book('book1', 340)
print(book1)
print(book1)


# Otro ejemplo de str 

class Author:
    def __init__(self, id, nif, email, year, city, num_books=0):
        self.id = id
        self.nif = nif
        self.email = email
        self.year = year
        self.city = city
        self.num_books = num_books

    def __str__(self):
        return f"Author con id = {self.id} " \
            f"nif = {self.nif} " \
            f"email = {self.email} " \
            f"year = {self.year} " \
            f"city = {self.city} " \
            f"num_books = {self.num_books}"
    

        return  '%s is smaller than %s' %('one', 'two')

author1 = Author(1, '2322323R', 'author1@email.com', 2000, 'Madrid')
print(author1)