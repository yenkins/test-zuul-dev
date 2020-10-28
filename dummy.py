from random import randrange

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
class Mammal(object):
    nlimbs = 4
    def __init__(self):
        print "I'm a mammal!"

class Cat(Mammal):
    # To-do: kill this class
    def __init__(self, color="calico"):
        self.color = color
        super(Cat, self).__init__()
        print "I have {0} legs I am {1}".format(self.nlimbs, self.color)

class FiveLeggedCat(Cat):
    nlimbs = randrange(10)

class Cat(Animal):
    def __init__(self, talk='meow', num_legs=4):
        print 'Hay cat'
        self.talk = talk
        super(Cat, self).__init__(num_legs)
