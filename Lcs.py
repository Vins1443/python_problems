#Largest common Substring

def lcs(s1,s2,index1,index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + lcs(s1, s2, index1+1, index2+1)
    
    else:
        op1 = lcs(s1, s2, index1, index2+1)
        op2 = lcs(s1, s2, index1+1, index2)
        return max(op1, op2)
    
    
print(lcs("elephant", "eretpat", 0, 0))    

def findLCS(x,y,m,n):
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]:
        return 1 + findLCS(x,y,m-1, n-1)
    else:
        return max(findLCS(x,y,m,n-1), findLCS(x,y,m-1,n))


x = "elephant"
y = "eretpat"

print(findLCS(x,y,len(x),len(y)))            
    
    
    
    