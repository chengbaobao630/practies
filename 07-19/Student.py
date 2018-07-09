from datetime import datetime


class Person(object):

    def __init__(self):
        print("person init")
        self.__birth = datetime.now()

    def birth(self):
        return self.__birth


class Man(object):

    def __init__(self):
        print(r"i'm a man")


class Student(Man, Person):

    def __init__(self, name="default"):
        Man.__init__(self)
        Person.__init__(self)
        print("student init")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


s = Student()
s.name = "cc"
print(s.name)
s.age = 99
print(s.age)
p = Person()
print(p.birth())
print(s.birth())

