class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return list(set([c.book for c in self.contracts()]))
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([c.royalties for c in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return list(set([c.author for c in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Must be an instance of Author.")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Must be an instance of Book.")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]