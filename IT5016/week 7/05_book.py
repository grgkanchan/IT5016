class Book():
    def __init__(self,title,author,publicationyear):
        self.title = title
        self.author = author
        self.publicationyear = publicationyear
        self.availability = True
    def display(self):
        print(f"Details\n Title: {self.title} \n Author: {self.author} \n Publication Year = {self.publicationyear} \n" 'Available' if self.availability else "Rented")

Info = Book("Gita","Bible",1965)
Info.display()

