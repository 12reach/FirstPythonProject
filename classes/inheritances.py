#!/usr/bin/python3

class AllUsers:

    def __init__(self):
        pass

    def Register(self):
        print("Please Register")

    def Login(self):
        print("Welcome Member.")

class Admin(AllUsers):

    def __init__(self):
        pass

    def Register(self):
        print("Admins need not register")

    def Login(self):
        print("Welcome Admin")

class Members(AllUsers):

    def __init__(self):
        pass


def main():

    admin = Admin()
    admin.Register()
    admin.Login()

    member = Members()
    member.Register()
    member.Login()


if __name__ == "__main__":
    main()

