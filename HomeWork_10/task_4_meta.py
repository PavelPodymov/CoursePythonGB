"""MetaClass"""


class MyMetaClass(type):
    """MetaClass for new class"""
    _instance = None

    def __new__(cls, name, bases, dct):
        """new"""
        if cls._instance is None:
            cls._instance = super().__new__(cls, name, bases, dct)
        else:
            return cls._instance


class Test(metaclass=MyMetaClass):
    """class Test"""
    pass


TestObj = Test
TestObject = Test
TestObjects = Test
print(TestObj is TestObject is TestObjects)




