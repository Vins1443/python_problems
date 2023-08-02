from array import *

my_array = array('i',[1,2,3,4,9])

for i in range(len(my_array)):
    print(my_array[i])

print(my_array[0])

my_array.append(8)
print(my_array)

my_array.insert(4,55)
print(my_array)

my_array1 = array('i',[464,66,80780,9686,99])
my_array.extend(my_array1)
print(my_array)

tempList = [242,87685,696,986787,6798]
my_array.fromlist(tempList)
print(my_array)

my_array.pop()
print(my_array)

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)


    