class Person:

    def __init__(self):
        age = 20
        Name = "John"

    def greeting(self):
        print("Hello")

    def press_on_the_tail_of_cat(self):
        Animal().sayMau()
class Animal:
    def __init__(self):
        type = "cat"
        name = "Murka"
    def sayMau(self):
        print("MAAAAAU!!!!")


Person = Person()
Person.press_on_the_tail_of_cat()