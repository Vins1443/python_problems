def numberFactor(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            p1 = numberFactor(n-1, tempDict)
            p2 = numberFactor(n-3, tempDict)
            p3 = numberFactor(n-4, tempDict)
            tempDict[n] = p1 + p2 + p3
        return tempDict[n]
    
    
#Bottom-up Approach

def numberFactorBU(n):
    tempArr = [1,1,1,2]
    for i in range(4, n+1):
        tempArr.append(tempArr[i-1] + tempArr[i-3] + tempArr[i-4])
        
    return tempArr[n]

print(numberFactorBU(5))            