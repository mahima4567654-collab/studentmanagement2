# Library Book Management System using OOP

class Book:
    def __init__(self, book_id, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Book ID : {self.book_id}")
        print(f"Book Name : {self.book_name}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        print("-" * 30)                                                

     
