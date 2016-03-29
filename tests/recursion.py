#!/usr/bin/python3

class Recursions:

    __inputs = "Give any number to see how countdown works."

    def __init__(self):
        print("Hi I an recursion class.")
        print(self.__inputs)

    def countDown(self, getNumber):
        self.inputs = getNumber
        inputs = int(getNumber)

        if inputs == 0:
            print("Started.")
        else:
            print(inputs)
            inputs = inputs -1
            self.countDown(inputs)







