# # class Something():
# #   def __init__(self,name,age,address,phone):
# #     self.name = name
# #     self.age = age
# #     self.address = address
# #     self.phone = phone
# #
# # p1 = Something("Mudassir", 25, "Bangalore", 9741843488)
# # print(p1.name)
# # print(p1.age)
# # print(p1.address)
# # print(p1.phone)
#
#
#
# # class Person():
# #   def __init__(self,name,age,address):
# #     self.name = name
# #     self.age = age
# #     self.address = address
# #
# #   def myfun(self):
# #     print("Hello my name is " + self.name + ". I am " + str(self.age) + " years old")
# #     print(self.address)
# #
# # p1 = Person("Mudassir", 25, "Bangalore")
# # p1.myfun()
#
#
# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname
# #
# #   def printname(self):
# #     print(self.firstname, self.lastname)
# #
# # x = Person("John", "Doe")
# # x.printname()
#
#
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 2
#     return x
#


# myclass = "Mudassir"
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# 
# myfunc()


# def factorial(n):
#   # single line to find factorial
#   return 1 if (n == 1 or n == 0) else n * factorial(n - 1);
#
#
# # Driver Code
# num = 5;
# print("Factorial of", num, "is",
#       factorial(num))

# def something(x,y):
#   x = str(input("Enter the string"))
#   y = str(input("Enter the string"))
#
#   res = x+y
#   print(res)
#
#
# something("input_str1","input_str2")

def fib(n):
  a=0
  b=1
  for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
fib(11)

def addition(num1,num2):
  result = num1+num2
  return result

num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))

result = addition(num1,num2)
print(result)

str = input("Enter your string")
if str==str[::-1]:
  print("String is polindrome")
else:
  print("String is not polindrome")


def factorial(n):
  return 1 if(n==0 or n==1) else n*factorial(n-1);
n=5
print("Factorial of ", n ," is", factorial(n))

a = int(input("Enter the number"))

def something(a):
  if a%2==0:
    print("Even number")
  else:
    print("Odd number")
something(a)


def max_two(a,b):
  if a>b:
    print("a is greater")
  else:
    print("b is smaller")
max_two(20,10)


def str1(a,b):
  print(a+b)
str1("Mudassir","Khan")


oldlist = [10,92,23,6,7,9,4,5]
def sort_fun(newlist):
  for i in range(len(newlist)):
    for j in range(i+1,len(newlist)):
      if newlist[i] >newlist[j]:
        newlist[i],newlist[j] = newlist[j],newlist[i]
  return newlist
print(sort_fun(oldlist))


