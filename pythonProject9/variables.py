# def something(x):
#     return x[::-1]
# my_text = something("Mohammed mudassir")
# print(my_text)
#
# str = input("Enter the string : ")
# def polindrome():
#     if str==str[::-1]:
#         print("Is a polindrome")
#     else:
#         print("Not a polindrome")
#
# polindrome()
#
# def addition(a,b):
#     result = a+b
#     return result
# a = int(input("Enter the 1st number"))
# b = int(input("Enter the 2nd number"))
#
# result = addition(a,b)
# print(result)
#
# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1);
# n = int(input("Enter the number"))
# print("Factorial of ", n, "is", factorial(n))
#
# def fib(n):
#     a=1
#     b=0
#     for i in range(0,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(8)
#
#
# a = int(input("Enter the 1st number"))
# b = int(input("Enter the second number"))
# def max_num(a,b):
#     if a>b:
#         print("a is greater")
#     else:
#         print("b is greater")
#
# max_num(a,b)
#
#
# n = int(input("Enter the table number"))
# def tables():
#     for i in range(1,11):
#         print(n,'*',i,'=', n*i)
# tables()
#
#
# def get_movie_tickets(movie_name,screen_number,time,date,seat_num):
#         print("movie name is :",movie_name,"screen number: ",screen_number,"show time : ",time,"date: ",date,"seat number: ",seat_num)
#
# get_movie_tickets("Goli mar",3,"11 am","18 aug 2020",43)
#
#
#
# sum = lambda n1, n2, n3, x, y: n1 + n2 + n3 + x + y
# print("using lambda sum of numbers:", sum(10, 50, 5, 6, 9))
#
#
# def lambda1():
#     sum = lambda n1,n2,n3,x,y,z: n1+n2+n3-x*y/z
#     print("Using lambda sum of numbers is: ", sum(10,23,42,19,5,7))
# lambda1


def add(datatype, *args):  # **kwargs
    if datatype =='int':   # if datatype is int, initialize answer as 0
        answer = 0

    if datatype =='str':  # if datatype is str, initialize answer as ''
        answer =''

    for x in args:
        answer = answer + x

    print(answer)

# Integer
add('int', 5, 6, 7 , 8)

# String
add('str', 'Hi ', 'Good ', 'morning')



class cars:
    def __init__(self,windows,doors,enginetype):
        self.__windows = windows
        self.__doors = doors
        self.__enginetype = enginetype

audi = cars(4,4,"petrol")
print(dir(audi))


#self.windows :  Public variable
#self._windows :  Protected variable
#self.__windows :  Private variable

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration
values = TopTen()

for i in values:
    print(i)

