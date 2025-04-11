#
# Library.py: Library management system
#
class Author():
        myclass = 'Author'

        def __init__(self, name, surname):
            self.name = name
            self.surname= surname 

        def __str__(self):
            return(self.name+ '|' +self.surname)

class Book():
        myclass = 'Book'

        def __init__(self, title, author, year):
            self.title = title 
            self.author = author
            self.year = year

        def displayBook(self):
            print('title: ', self.title)
            print('\tauthor: ', self.author, '\tyear: ', self.year)

class comedy(Book):
    myclass = 'Comedy'

    def __init__(self, title, author, year, type):
        super().__init__(title, author, year)
        self.type = type 

    def displayBook(self):
        super().displayBook()
        print('\t Type: ',self.type)


class fiction(Book):
    myclass = 'Fiction'

    def __init__(self, title, author, year, type):
        super().__init__(title, author, year)
        self.type = type

    def displayBook(self):
        super().displayBook()
        print('\t Type: ', self.type)

class sciencefiction(fiction):
    myclass = 'Science Fiction'

    def __init__(self, title, author, year, type):
         super().__init__(title, author, year, type)
         self.type = type
    def displayBook(self):
         super( ).displayBook()


