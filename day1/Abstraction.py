# Abstraction means : Hiding the internal details and showing only the essential features of the object.
# In Python, abstraction can be achieved using abstract classes and methods provided by the abc module. 
# @abstractmethod decorator is used to declare a method as abstract.
from abc import ABC, abstractmethod
class Animal(ABC):  # Abstract class inheriting from ABC
    @abstractmethod
    def sound(self):  # Abstract method
        pass  # null value or pass to its implementation in derived class

    @abstractmethod
    def habitat(self):  # Abstract method
        pass

class Dog(Animal):  # Derived class inheriting from Animal
    def sound(self):  # Implementing abstract method
        return "Bark"

    def habitat(self):  # Implementing abstract method
        return "Domestic"
class Lion(Animal):  # Derived class inheriting from Animal
    def sound(self):  # Implementing abstract method
        return "Roar"

    def habitat(self):  # Implementing abstract method
        return "Wild"
# create instances of derived classes
dog = Dog()
lion = Lion()
# access methods
print("Dog Sound:", dog.sound())  # Output: Bark
print("Dog Habitat:", dog.habitat())  # Output: Domestic    
print("Lion Sound:", lion.sound())  # Output: Roar
print("Lion Habitat:", lion.habitat())  # Output: Wild
