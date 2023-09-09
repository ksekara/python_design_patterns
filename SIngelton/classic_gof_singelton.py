class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        print('<init> called ..')
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        print('<get_instance> called ... ')
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance


s0 = ClassicSingleton.get_instance()
s1 = ClassicSingleton.get_instance()

print(s0)
print(s1)