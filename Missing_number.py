def missingNumber(myList, totalCount):
    expected_sum = totalCount * ((totalCount+1)/2)
    actual_sum = 0

    for i in myList:
        actual_sum += i
    return int(expected_sum - actual_sum)

print(missingNumber([1,2,3,4,5,6,8],8))

    
    