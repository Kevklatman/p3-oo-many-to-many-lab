class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be type of string.")
        self.name=name



class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be type of string.")
        self.title=title


class Contract:
    def __init__(self, author, book, date, royalties):
        if not isinstance(date, date):
            raise TypeError("Value is not a valid date.")
        self.date=date
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer.")
        self.royalties=royalties
        
