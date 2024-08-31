from datetime import datetime

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self.author = author

        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")
        self.book = book

        if not isinstance(date, str):
            raise TypeError("Date must be a string.")
        self.date = date

        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer.")
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]