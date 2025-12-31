# lst = [1, 2, 3]
# my_str = "mlops playlist"

# my_int = 155

# print(type(my_int))

# my_str = my_str.capitalize()
# # lst.clear()
# # print(lst)

# print(my_str)

# a = 'x'
# b = 'y'

# print(a + b)

# from oops_projects import chatbook

# user1 = chatbook()


# functions vs method below.
# lst = [1, 2, 3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
# user1.sendmsg()

from oops_projects import chatbook

# # Getter and setter methods example
# user1 = chatbook()
# print(user1.get_name())

# user1.set_name("Agent X")
# print(user1.get_name())

user1 = chatbook()
print(user1.id)


# using static method directly from class rather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
# print(user1.id)

user3 = chatbook()
print(user3.id)

# user3 = chatbook()
# print(user3.id)
