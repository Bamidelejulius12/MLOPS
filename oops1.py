# initate class 
class employee:
    # special methos/ magic method / dunder method - constructor
    def __init__(self):
        # print("started execueting attributes/data")
        # print(id(self))
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
       #  print("attributes/data")

    def travel(self):
        print("This travel method was called manually")
        print(f"employee is travelling to dehil")
    


# create an obj/instance of the class
sam = employee()
# sam.name = "samuel"
# #print(id(sam))
# print(sam.name)

# shakiman = employee()
# print(id(shakiman))
# # # print(sam.salary)
# sam.travel()
# # print(type(sam))