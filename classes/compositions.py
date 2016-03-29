#!/usr/bin/python3

class Parent:

    def __init__(self):
        pass

    def ParentImplicit(self):
        print("This is parent implicit.")


class Child:

    def __init__(self):
        pass

    def ChildImplicit(self):
        print("THis is child implicit.")
        print("Composition of parent.")
        Parent.ParentImplicit("child")

parent = Parent()
child = Child()
parent.ParentImplicit()
child.ChildImplicit()