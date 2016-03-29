#!/usrbin/python3

class Table:

    def __init__(self):
        pass

    # def ItHolds(self):
    #     print("A table holds books, writing pads on it.")
    #
    # def YouCanWriteOnit(self):
    #     print("You can write on a table.")

    def Get(self):
        print("Please get me that table.")

    def Put(self):
        print("Please put the table on the corner of the room.")


    def Destroy(self):
        print("Some people came and they did not want us to read and write. They destroted the table.")



class Book:

    def __init__(self):
        pass

    # def ItHelps(self):
    #     print("A book helps us to know something new.")

    def Get(self):
        print("Please get me that book.")

    def Put(self):
        print("We put some new books on the table.")

    def Destroy(self):
        print("Some people came and they did not want us to read and write. They destroted the book.")



def main():

    MyTable = Table()
    MyBook = Book()

    InMistake(MyBook)
    Intentionally(MyTable)


def InMistake(Table):
    Table.Get()
    Table.Put()
    Table.Destroy()

def Intentionally(Book):
    Book.Get()
    Book.Put()
    Book.Destroy()


if __name__ == "__main__":
    main()
