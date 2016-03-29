#!/usr/bin/python3

class Dog:

    name = None

    def __init__(self, **kwargs):
        self.properties = kwargs

    def get_properties(self):
        return self.properties

    def set_properties(self, key):
        self.properties.get(key, None)


    @property
    def Color(self):
        return self.properties.get('color', None)

    @Color.setter
    def Color(self, color):
        self.properties['color'] = color

    @Color.deleter
    def Color(self):
        del self.properties['color']

def main():

    lucky = Dog(nature = 'obedient')
    print(lucky.properties.get('nature'))
    # now we are going to us the decorator function as a normal property
    lucky.Color = 'black and yellow'
    print(lucky.Color)
    lucky.name = 'luckybaba'
    print(lucky.name)

if __name__ == "__main__":
    main()
