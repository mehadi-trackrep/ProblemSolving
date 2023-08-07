import time

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        print('Singleton.__init__ called')
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class TestClass(metaclass=Singleton):
    """
    Example class.
    """

    def __init__(self):
        print('TestClass.__init__ called')

    def get__str__(self):
        return 'TestClass'

if __name__ == '__main__':
    t1 = TestClass()
    print("t1 done!")
    time.sleep(5)
    t2 = TestClass()
    print("t2 done!")
    print(t1 is t2)
    print(id(t1), id(t2))
    print(t1, t2)
    #-------------------
    print(t1.get__str__())
    print(t2.get__str__())