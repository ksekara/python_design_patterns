class SingletonMeta(type):
    _instance = {}

    # override the __new__ method instance the class at load time
    def __new__(cls, *args, **kwargs):
        print('initializing <super>...')
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instance[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('initializing <child>...')
        # Initialize your attributes here
        self.attribute = "I'm a singleton"