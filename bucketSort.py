import math
from insertion_sort import insertionSort

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([]) #appending number of buckets in array making it a 2d array
    for j in customList:
        index_b = math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


cList1 = [2,1,7,6,5,3,4,9,8]
print(bucketSort(cList1))


cList = [2,1,6,3,7,9,111]