def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)            


cList = [2,1,6,3,7,9,111]   
bubbleSort(cList) 