# Single or basic Inheritance

# base class
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"hello, my name is {self.name}")

# # derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # create an instance of child
# child = Child("Alice")
# child.greet()
# child.play()

# MULTILEVEL INHERITANCE
# Base class

# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story")

# # intermediate class
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working")

# # Derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # create an instance of child
# child = Child("charlie")
# child.tell_story()
# child.work()
# child.play()


# Hierarchical Inheritance

# base class
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
    
# # Derived class 1    
# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# # Derived class 2
# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying")

# # create instances of child1 and child2
# child1 = Child1("dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

# Multiple Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A {self.name}")

# intermediate class 1
class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

# Derived class
class D(B, C):
    def greet(self):
        print(f"Hello from D {self.name}")
        super().greet()

d = D("Frank")
d.greet()