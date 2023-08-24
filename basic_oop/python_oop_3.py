from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} says: {self.sound()}")


class Dog(Animal):
    def sound(self):
        return "Woof!"

    def description(self):
        super().description()


class Cat(Animal):
    def sound(self):
        return "Meow!"

    def description(self):
        super().description()


dog = Dog()
dog.description()

cat = Cat()
cat.description()
