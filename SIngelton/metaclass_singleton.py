class SingletonMeta(type):
    _instance = {}

    def __call__(cls):
        print('<call meta> calling...')
        if cls not in cls._instance:
            instance = super().__call__()
            cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        ...


s1 = Singleton()
s2 = Singleton()


