class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")


# Create an object of Greeting class
greeting = Greeting("Kalindu")
greeting.say_hello()
