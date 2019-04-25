# h = 50
# if h > 50:
#     print("x")
# elif h < 20:
#     print("xx")
# else:
#     print("xxx")


# c = 5
# while c != 0:
#     print(c)
#     c -= 1

# c = 5
# while c:
#     print(c)
#     c -= 1


# d = {"alice": '1111'}
# #print(d)
#
# d['alice'] = '2222'
# #print(d)
#
# d['charles'] = '3333'
# print(d)


# cities = ["London", "New York"]
# for city in cities:
#     print(city)

# cities = {"London": 1, "New York": 2}
# for city in cities:
#     print(city, cities[city])


# def covert(s):
#     """test"""
#     x = -1
#     try:
#         x = int(s)
#         print("succeeded", x)
#     except ValueError:
#         print("failed")
#     except TypeError:
#         print("failed2")
#     return x

# def covert(s):
#     """test"""
#     try:
#         return int(s)
#     except (ValueError, TypeError) as e:
#         print("error: {}".format(str(e)))
#         return -1


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#
#     def welcome(self):
#         print("welcome", self.firstname, self.lastname)
#
#
# x = Student("Mike", "Olsen")
# x.welcome()


# import mymodule
#
# mymodule.greeting("Jonathan")

# import mymodule as mx
#
# a = mx.person1["age"]
# print(a)

# from mymodule import person1
#
# print(person1["age"])


# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])

# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)

# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# # use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))


# f = open("demofile.txt", "r")
#
# print(f.read())

# f = open("demofile.txt", "r")
# for x in f:
#   print(x)

# f = open("demofile.txt", "r")
#
# print(f.readline())
#
# f.close()

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


#f = open("myfile.txt", "x")
#f = open("myfile.txt", "w") #Create a new file if it does not exist: