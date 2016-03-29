#!/usr/bin/python3

# this is fish class and we will have some base classes from it

class fishClass:
    pass

class ChildFish(fishClass):
    print("Hi I am a child fish and I came from troubled water.")

fan1 = ChildFish()

print(fan1)
 # the output looks like thsi Hi I am Salman Khan and I am a fish from troubled water.
# <__main__.salmanFish object at 0xb7275b4c>

# now we are going to change the fish class a little bit

class myFishClass:

    fin = "I am fin and I come to use when a fish swims."
    def __init__(self):
        print("Hi I am a parent fish of all child classes.")

    def swim(self, distance, time):
        self.distance = distance
        self.time = distance * time
        return distance, time
    # print("The fish takes", time, "minutes to swim ", distance, "KMs.")

# let us have some instances of myFish

fish1 = myFishClass()
# once we crate this instance,

print("What does the fins do?")
print(fish1.fin)
# now this is attribute or a property of a fish
# there could be more attributes like this

# let us see whether fish can swim or not and what time it takes to traverse a certain distance
# this is the method or function part of the class which has already got a blueprint

print("To swim 1 KM the first fish takes 10 minutes.")
print("Fish1 : ")
fish1.swim(10, 10)
print("To travel ", fish1.distance, "kms")
print("Fish1 takes", fish1.time, "minutes.")

print("Suppose the fish1 starts with 10 kms per minute speed. But with the increase of each km it starts reducing 1 minute"
      "in its speed and loses breadth.")

print("Give any number and see what happens.")
inputs = input(">>>>>>>")
# print(inputs)
fish1.distance = 0
for fish1.distance in range(0, int(inputs)):
    # if the fish starts with 10 kms per minute
    # and with the increase of each km it starts reducing 1 minute

    fish1.time = 10
    fish1.time = fish1.time - fish1.distance
    if fish1.time == 0:
        # it loses its breadth at the point of
        print("After", fish1.distance, "kms, it gets drowned. The fish is dead.")
        break
    else:
        continue

if fish1.time <= 10:
    print("Upto 10 kms the fish is saved.")