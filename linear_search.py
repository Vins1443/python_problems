def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
        
    return -1    
        
print(linearSearch([3678648,767,89,7968,5676], 767))        