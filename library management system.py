#Implement a student library system using oops where students can borrow a book from list of books.
# Creating a separate Library and student class.This program is menu driven. 
#Library management System using python.

class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def display(self):
        print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ ")
        print("Books present in the library are: ")
        for book in self.books:
            print("\t -> " +book)
        print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ ")
    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. please keep it safe and return it within 14 days.Thank You!!")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. please wait until the books is returned. Thank You!!")  
            return False
    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading  it. Have a great day ahead!")          

class Student:
    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book


if __name__=="__main__":
    centralLibrary=Library(['Data Structures','Algorithms','System programming','Software Engneering','Complex variables','Differential Equations','Computer Organiztion and Architecture','Introductuion to Discrete Mathematics','Oops','Django','clrs','pthon'])
    # centralLibrary.display()
    student=Student()
    while(True):
        welcomeMsg=''' __________________________________________WELCOME TO CENTRAL LIBRARY______________________________________________
        please choose one option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
       '''
        print(welcomeMsg)
        a=int(input("Enter a choice: "))
        if a==1:
            centralLibrary.display()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())    
        elif a==3:
            centralLibary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing central Library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")            
        