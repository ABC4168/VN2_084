#Table of the given number using functions
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
n=int(input("Enter the table number : "))
table(n)


#multiply all the numbers in a list,set,tuple
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

# Sum of all number in list.
def addition(myList):
    result = 0
    for x in myList:
        result = result + x
    return result
list2 = [1, 2, 3]
print(addition(list2))


#Sum of all number in Tuple.
def addition(myTuple):
    result = 0
    for x in myTuple:
        result = result + x
    return result
list2 = (1, 2, 3)
print(addition(list2))


# Sum of all number in list.
def addition(mySet):
    result = 0
    for x in mySet:
        result = result + x
    return result
list2 = {1, 2, 3}
print(addition(list2))


#multiply all the numbers in a tuple
def multiplytuple(value):
    res = 1
    for element in value:
        res *= element
    return res
tuple1 = (7, 8, 4, 7, 8)
res = multiplytuple(list(tuple1))
print("The product of tuple elements are : " ,res)


#Accepts a string and calculate the numbers of upper-case letter and lower case letters
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:", count1)
print()
print("The number of uppercase characters is:", count2)
print()



#Take a list and return a new list with unique elements of the first list
def unique_list(list):
  a = []
  for unique in list:
    if unique not in a:
      a.append(unique)
  return a
print(unique_list([1,2,3,3,3,3,4,5,6,6,0,9,9,0]))



#Print given Pascal's triangle
n = 5
for i in range(n):
    print(' ' * (n - i), end='')
    print(' '.join(map(str, str(11 ** i))))


# Function to check whether a string is a palindrome or not
string = input(("Enter a string:"))
if string == string[::-1]:
    print("Is a palindrome")
else:
    print("Is not a palindrome")


#check whether a number is in a given range
def test_range(n):
    if n in range(3,9):
        print(n,"is in the range",)
    else :
        print("The number is outside the given range.")
test_range(11)