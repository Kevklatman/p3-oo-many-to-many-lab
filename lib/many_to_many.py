class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be type of string.")
        self.name=name
all =[]



class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be type of string.")
        self.title=title
all = []


class Contract:
    def __init__(self, author, book, date, royalties):
        pass
all = {}