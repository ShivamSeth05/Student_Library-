class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayBooks(self):
        print("\nBooks present in this library  are :\n")
        for book in self.books:
            print(" *"+book)
            # print()

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} .Please keep it safe and return in within 30 days\n\n\t Thank you for visiting here. ")
            self.books.remove(bookName)
            return True
        else:
            print("\nSorry, This book has already bee issued to someone. Please wait.\n \n\tThank you !")
            return False

    def returnBooks(self,bookName):
        self.books.append(bookName)
        print("Thanks for returing Or this book! Hope You you enjoyed reading it. have a Great Day ahead..")
    def addBooks(self,bookName):
        self.books.append(bookName)
        print("Thanks for adding this book! have a Great Day ahead..")
        

class Students:
    def req_books(self):
        self.rq_book=input("Enter the book name :")
        with open("Student_detail.txt","a")as f:
                f.write(f" Student Name :{Stu_Name}\tRoll Number:{Stu_RegNo} \tand Issued Book :{self.rq_book}\n")
        return self.rq_book

    def return_books(self):
        self.return_book=input("Enter the book name :")
        return self.return_book
    def add_books(self):
        self.add_book=input("Enter the book name :")
        return self.add_book

if __name__ == "__main__":
    f=open("Student_detail.txt","w+")
    f.write("==INFORMATION OF STUDENT== \n")
    f.close()
    # Available books in Cenral library
    Student= Students()
    CentralLibrary = Library(['Algorithms', 'Advance_java', 'Python'])
    
    while(True):

        msg= ('''\n\n\t\t\t=======Welcome to Central Library=======\n
        =====MENU=====
        1.List all the Books 
        2.Request of books
        3.Return of books
        4.Add the book in Central Library
        5.Exit ''')
        print(msg)
        ch = int(input("Enter a choice "))
        if ch == 1:
            CentralLibrary.displayBooks()
        elif ch==2:

            Stu_Name=input("\n====Fill Some Details here=== \nPlease Enter Your Name: ")
            Stu_RegNo=input("Roll Number :")

            CentralLibrary.borrowBook(Student.req_books())
        elif ch==3:
            CentralLibrary.returnBooks(Student.return_books())

        elif ch==4:
            CentralLibrary.addBooks(Student.add_books())
            # input("\nEnter the book name:")

        elif ch==5:
            print("Have a Great Day Ahead")
            exit()

        else:
            print("Invalid Choice!")

