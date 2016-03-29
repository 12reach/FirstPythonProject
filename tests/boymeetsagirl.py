#!/usr/bin/python3

# i always believe that coding is like writing

################
# a boy met a girl. The boy fell in love. The girl did not. She hated him. Because the boy was ugly.
################

# let us convert this sentence to an interactive program where you can change the course of story
# according to your wish

# boy and girl are child-class of humans class but they have their own features
# they have properties like beauty
# they have methods like love, hate etc

class humansClass:

    def __init__(self, gender = 'humans', name = 'name'):
        self.gender = gender
        self.name = name

    def whatGender(self):
        return self.gender

    def whatName(self):
        return self.name

    def lookOfHumans(self, look = "bad"):
        self.look = look
        return look



def main():
    inputs = input("Type boy.\n")
    if inputs == 'boy':
        print("You chose", inputs)
        nameOfBoy = input("Now give a name")
        print("You gave name", nameOfBoy, "to your", inputs)
        nameOfGirl = input("Now you give a name to your girl.")
        print("You gave a name", nameOfGirl, "to your girl.")
        boy = humansClass('boy', nameOfBoy)
        girl = humansClass('girl', nameOfGirl)
        print("Now it is final that you chose a", boy.whatGender(),
              "of name", boy.whatName(), "and a", girl.whatGender(),"of name", girl.whatName(),
              ". Now,", boy.whatName(), "fell in "
              "love of", girl.whatName(), ".")
        print("Now a problem arises that you can solve.")
        print(boy.whatName(), "does not look good. Do you want to rectify it?")
        print("If you want to make", boy.whatName(), "looks good, just type 'yes' and if don't want type 'no'")
        lookOfBoy = input("Type either 'yes' or 'no'.")
        if lookOfBoy == 'yes':
            print("You wanted to look", boy.whatName(), "looks good.")
            print(girl.whatName(), "wanted the same. And the story becomes stereotyped.")
        else:
            print("You did not want to see the boy looking good. Now the story turns out to be interesting.")





if __name__ == "__main__":main()