# strings
txt = "Hello All"
# print(txt[-2] + txt[2])
#  \n  \r  \u2028
# print(txt.count("l"))

# print(txt.rfind("q"))

# print(txt.index("q"))

# my_dictionary = str.maketrans("l","q", "a")
# my_dictionary = str.maketrans({
#     "l":"q",
#     "h": "a",
#     "a":"b"
# })
# new_txt = txt.translate(my_dictionary)

# print(new_txt)
# print(txt.swapcase())
# data = ("q", "h", "A")
# print(txt.startswith("H", 2))
# print(txt.startswith(data))

# password = "  d   "
# print(password.isdigit())
# print(password.isalnum())
# print(password.isalpha())
# print(password.islower())
# print(password.isupper())
# print(password.istitle())
# print(password.isspace())


# txt = "hello all"
# x = 5
# print( "h" in txt) 
# print( "h" not in txt) 

# print("%s i have data with %d" %(txt, x))

# print("%s i have data with %s" %(txt, x))

# lists
# x = [10, "marwa", True]
# print(x)

# x= [None] * 5
# x[2] = "hello"
# print(x[-1])
# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# for w in words:
#     print(w)

# del(words[4])
# print(words)
# print(len(words))
# del(words)
# print(words)
# x = words[0:3]
# y = x+words
# print(y)

# a= "apple"
# print(a in words)

# append

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "apple"]
# a =[1,2,3]
# words.append(10)
# words.extend(a)
# words.insert(5, 7)
# words.pop(2)
# x = words.copy()
# print(words.count("apple"))

# print(len(words))

# words.remove("a")
# words.reverse()
# words.sort(reverse=False)
# print(words)

# numbers = [1,4,7,90,13]
# n1 = [1, 10, 90]
# evens = [n for n in numbers if n % 2 == 0]

# even = []
# for n in numbers:
#     if n % 2 == 0: 
#         even.append(n)

# for n in range(0,10):
    # [0,1,2,3,4,5,6,7,8,9]
    # print(n)
# numbers = [1,4,7,90,13, 4]
# i =0
# for n in numbers:
#     print(f"{n} - {i}")
#     i+=1


# n1 = [1, 4, 10, 2]
# n2 = [1, 5, 7, 10]
# c = [a for a in n1 if a in n2]

# t = (5, 3, "m",)
# print(t[0:2])

# t1 = ("10",) * 3
# print(t1)

# s = {1, 2, 3 , 4}
# print(tuple(s))

# s = { 1,2,1}
# print(tuple(s))
# s = {1,1,2,4,3,2,5,6,3}
# print(s[1])
# s.add("hello")
# s.discard(4)
# s.remove(1)
# s.clear()
# print(s.pop())
# print("----------------------")
# for a in s:
#     print(a)
# a = {1,2,3}
# b={1,5,2}
# # n = a.difference(b)
# n = a.intersection(b)
# print(n)
# a = [1,2,3]
# b = [2,3,5]
# n = list ( set(a).intersection(set(b)) )
# print(n)


# dictionary
# data = {
#     1: "a",
#     2: "b", 
#     3: "c",
#     "z": "skam"
# }
# print(data["z"])
# data[50] = 4
# del data["z"]
# print(data)

# print(3 in data)
# data.clear()
# print(data)

# c = data.copy()
# c = data
# del data[1]
# print(c)
# print(data)
# print(data.popitem())
# print(data)
# print(data.pop(7, "not found"))
# print(data)

# data = {
#     "name": "Alice",
#     "age": 28,
#     "city": "New York",
#     "country": "USA",
#     "email": "alice@example.com",
#     "is_student": False,
#     "height_cm": 165,
#     "hobbies": ["reading", "traveling", "music"],
#     "favorite_color": "blue",
#     "member_since": 2019
# }

# print(data.get("ages", "not found"))
# print(data.keys())

# for a in data.keys():
#     print(data[a])

# print(data.values())


# print(data.items())

# prompt enter user data
# name age email
# 10 times
# users 
# user 1: name: marwa age:40 email: marwa@test.com


# t = (1,5,6)
# d = dict.fromkeys(t, 0)
# print(d)

# d.setdefault(4)
# print(d)

# def fun():
#     print("hello")

# fun()

# def greet_user(userName="a"):
#     """function for greeting"""
#     print(f"hello {userName}")

# greet_user("marwa")

# print(greet_user.__doc__)

# greet_user()


# def show(name, age):
#     print(name, age)

# show(age=40, name="marwa")

# def pr(*data):
#     print(sum(data)/len(data))

# pr(11,2,3,66)


# x = 1

# def test():
#     global x
#     x= 5
#     print(x)

# test()

# print(x)


# users = []
# for i in range(1,2):
#     print(f'Enter user {i} Data')
#     users.append ({
#         "name": input("name value: "),
#         "age": input("age value: "),
#         "email": input("email value: "),
#     })
# i=1
# for u in users:
#     print(f"user number { i }")
#     print(f"name: {u["name"]}\nage:{u["age"]}\nemail:{u["email"]}")
#     print("--------------------------------------------------------")
#     i+=1

# def is_eligable(userData):
#     return int(userData["age"]) >= 21

# def print_user(userData):
#     print(f"name: {userData["name"]} - age:{userData["age"]} - email:{userData["email"]} - can vote: {is_eligable(userData)}")
#     print("--------------------------------------------------------")

# def get_user_data():
#     userData = {
#         "name": input("name value: "),
#         "age": input("age value: "),
#         "email": input("email value: "),
#     }
#     return userData

# users = []
# for i in range(1,3):
#     users.append(get_user_data())

# for u in users:
#     print_user(u)


# sq = lambda x:x**2
# sq(5)

# even_odd = lambda a: "Even" if a % 2 == 0 else "Odd"
# print(even_odd(10))

# import datetime
# import calendar
# d = datetime.datetime.now()
# print(d)
# d = datetime.datetime(2025, 10, 30)
# print(d)
# our course start in 30, 10, 2025
# print( f" our course start in {d.year}, {d.month}, {d.day}" )
# print(d.strftime("%a"))
# print(d.strftime("%A"))
# print(d.strftime("%w"))
# print(d.strftime("%d"))
# print(d.strftime("%B"))
# print(d.strftime("%b"))
# print(d.strftime("%Y"))
# print(d.strftime("%H"))
# print(d.strftime("%c"))
# print(d.strftime("%x"))
# calendar.prcal(2010, w=6)
# print(calendar.isleap(2010))


# try:
#     print(x)
# except BaseException as myError:
#     print("error in printing", myError)
# else:
#     print("done")

# pip packages
def f(val):
    if(val<0):
        raise Exception("Error can't be negative")
    print(val)

try:
    f(-5)
except Exception as msg:
    print(msg)

import camelcase
c = camelcase.CamelCase()
txt = "marwa radwan"
print(c.hump(txt))

