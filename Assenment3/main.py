1.
list1 = [1,2,3,4,[5,6,7]]
for x in list1[4]:
 print(x)



2.
list2 = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'Mudassir Khan'}}}]
print(list2[0]['c'][2]["c"])
x = list2[0]['c'][2]["c"]
print({i:x.count(i) for i in x})



3.
list3= [
    ['a','b','c'],
    [4,5,6],
    ['x','y','z']]
transpose = [[row[i] for row in list3] for i in range(len(list3[0]))]
print(transpose)


4.
test_list1 = [1, 2, 3, 4, 5]
test_list2 = [10, 9, 8, 7, 6]
test_list3 = [5, 6, 7, 8, 9]
print("Original list 1 : " + str(test_list1))
print("Original list 2 : " + str(test_list2))
print("Original list 3 : " + str(test_list3))
list4 = []
for i in range(0, len(test_list1)):
       list4.append(test_list1[i] + test_list2[i] + test_list3[i])
print("Resultant list is : " + str(list4))



5.
mydict3 = {10:56, 10:4, 20:1, 20:9, 30:1, 50:6}
mydict4 = {}
for i in mydict3:
    if i in mydict4:
        mydict3[i] += 1
        mydict3.key=lambda x: x[1]
        print(mydict4)
    else:
        mydict3[i] = 1
print(mydict3)



6.
mydict2 = {1:'Mohammed', 'name':{'location':{'Shimoga', 'Bangalore'}, 'che':{1:{'ARMS', 'Khans'}}}}
nl = []
nl.append(mydict2[1])
nl.append(mydict2['name']['location'])
nl.append(mydict2['name']['che'][1])
print(nl)



7.
x = {}
n = int(input("Enter the elements to add : "))
for i in range(n):
       k = input('Enter key: ')
       v = input('Enter value: ')
       x[k] = v
print('Resultant output: \n', x)
