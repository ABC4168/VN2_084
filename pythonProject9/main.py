#
# a = 10
#
# def something():
#     global a
#     a = 15
#     print(a)
#
# something()
#
# print(a)
#

#global and local in te same function
a1 = 10
print(id(a1))
def something1():
     a1 = 9

     x = globals()['a1']
     print(id(x))
     print(a1)


something1()

print(a1)
