class SingletonMeta(type):
    _instance = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instance[cls] = super().__call__()
        print('initializing <super>...')

    def __call__(cls, *args, **kwargs):
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('initializing <child>...')
        self.attribute = "I'm a Singleton"



s1 = Singleton()
s2 = Singleton()

print(s1 is s2)