# initate class 
class employee:
    # special methos/ magic method / dunder method - constructor
    def __init__(self):
        print("started execueting attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"employee is travelling to {destination}")
    


# create an obj/instance of the class
sam = employee()
# # print(sam.salary)
sam.travel("kerala")
print(type(sam))