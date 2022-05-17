# def worst():
#     print("Hello world!")
# worst()
#
def reverse(str):
    return str[::-1]

mytext = reverse("Mohammed mudassir you are worst in practical ")
print(mytext)
#
#
# class something():
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#
#     def myfun(self):
#         print(self.name,self.address)
#
# p1 = something("Mudassir"," Bangalore")
# p1.myfun()
#
# # Arguments
# # Information can be passed into functions as arguments.
#
# def my_function(fname,lname):
#     print(fname + lname)
#
# my_function("Mudassir","Khan")
# my_function("Mohammed","khan")
#
# def addition(x,y):
#     res = x+y
#     return res
#
# x = int(input("Enter the 1st number"))
# y = int(input("Enter the 2nd number"))
#
# res = addition(x,y)
# print(res)
#
# str = input("Enter the string : ")
# def polindrome():
#     if str==str[::-1]:
#         print("Is a polindrome")
#     else:
#         print("Is not a polindrome")
#
# polindrome()
#
#
# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1);
#
# n = int(input("Enter the number"))
# print("Factorial of ",n," is", factorial(n))
#
# def fib(n):
#     a=0
#     b=1
#     for i in range(0,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(11)
#
# def something1(a):
#     if a%2==0:
#         print("Even number")
#     else:
#         print("odd number")
#
# something1(45)
#
# a = int(input("Enter the 1st number"))
# b = int(input("Enter the 2nd number"))
# def max_num():
#     if a>b:
#         print("a is greater")
#     else:
#         print("b is greater")
#
# max_num()
#
# a1 = int(input("Enter the 1st number"))
# b1 = int(input("Enter the 2nd number"))
# def operators():
#     a = a1+b1
#     b = a1-b1
#     c = a1*b1
#     d = a1/b1
#     print(a,b,c,d)
# operators()
#
# n = int(input("Enter the number"))
# n1 = int(input("Enter the number"))
# def tables():
#
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i,)
#
#
#     for i in range(1,11):
#         print(n1,'*',i,'=',n1*i)
#
# tables()

class Student():
    def __init__(self,name,address,age):
        self.name = name
        self.address = address
        self.age = age

    def myfun(self):
       print(self.name,self.address,str(self.age))

p1 = Student("Mudassir","Bangalore",25)
p1.myfun()

str1 = input("Enter the string : ")
def find_len(str):
    len = 0
    for char in str:
        len += 1
    return len
print("Length of string ", find_len(str1))
