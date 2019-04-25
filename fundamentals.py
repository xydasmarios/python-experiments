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


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

    def welcome(self):
        print("welcome", self.firstname, self.lastname)


x = Student("Mike", "Olsen")
x.welcome()
