myList = [1,2,3,4,5]

def middle(lst):
    l = len(lst)
    for i in range(l):
        return lst[i+1:l-1]
        
print(middle(myList))
print(len(myList)) 

myList2D = [[1,2,3],[4,5,6],[7,8,9]]

def sumDiagonal(a):
    s = 0
    for i in range(len(a)):
        s += a[i][i]

    return s    
print(sumDiagonal(myList2D))   

myL = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]