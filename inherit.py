# # Simple inheritance example

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         #self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived class
# class Dog(Animal):

#     def speak1(self):
#         print(f"{self.name} barks and bite.")

# # # create an instance of Animal
# # animal = Animal("Generic Animal")
# # animal.speak() # Output: Generic Animal makes a sound.


# # create an instance of Dog
# dog = Dog("buddy")
# dog.speak() # Output: Buddy barks.


# Super Keyword Example

# SUPER

class Animal:
    def __init__(self):
        self.name = "buddy"
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. it is a {self.breed}.")


# create an instance of Dog
dog = Dog("Golder retriever")
dog.speak()

