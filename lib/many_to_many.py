
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be type of string.")
        self.name=name
        Author.all.append(self)
    
    def contracts(self): #This method should return a list of related contracts.
        pass

    def books(self): #This method should return a list of related books using the Contract class as an intermediary.
        pass

    def sign_contract(book, date, royalties): #This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
        pass

    def total_royalties(): #This method should return the total amount of royalties that the author has earned from all of their contracts.
        pass





class Book:
    all = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be type of string.")
        self.title=title

class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(date, date):
            raise TypeError("Value is not a valid date.")
        self.date=date
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer.")
        self.royalties=royalties
        if not isinstance(author, str):
            raise TypeError("Author must be type of string.")
        self.author=author
        if not isinstance(book, str):
            raise TypeError("Book must be type of string.")
        self.book=book
        Contract.all.append(self)

    def contracts_by_date(cls, date): #A class method contracts_by_date(cls, date): This method should return all contracts that have the same date as the date passed into the method.


        



