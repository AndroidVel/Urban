import inspect
from pprint import pprint


def introspection_info(obj):
    dict_ = {'type': type(obj),
             'attributes': dir(obj),
             'methods': inspect.getmembers(obj, inspect.ismethod),
             'module': inspect.getmodule(obj),
             'is callable': callable(obj)}
    return dict_


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
info = introspection_info(p1)
pprint(info)
