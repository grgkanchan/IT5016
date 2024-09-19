class Library():
    def __init__(self):
        pass
    books = []
    patrons = []
    def add(self,title):
        if title not in self.books:
            self.books.append(title)
            print(f"{title} is added")
        else:
            print(f"No Books is Added.")
class Patron():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.patronbooks = []
    def newpatron(self,pname):
        if pname not in self.patronbooks:
            self.patronbooks.append(pname)
            print(f"{pname} has be added.")
        else:
            print("Nothing New.")
    def display(self,pname):
        if self.patronbooks:
            print(f"Registered patron: {pname}")
        else:
            print("Nothing is registered")