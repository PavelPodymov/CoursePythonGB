"""MetaClass"""


class MyMetaClass(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Test(metaclass=MyMetaClass):
    pass


TestObj = Test()
TestObject = Test()
TestObjects = Test()
print(TestObj is TestObject is TestObjects)
