

class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

obj1 = Foo.get_instance()
print(obj1)

obj2 = Foo.get_instance()
print(obj2)

obj3 = Foo.get_instance()
print(obj3)
