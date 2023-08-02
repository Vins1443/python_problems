# def factorial(n):
#     assert n>=0 and int(n) == n, 'The number must be a positive integer only'
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factorial(n-1)  

# print(factorial(-3))  

# nTerms = int(input("How many terms?"))

# n1, n2 = 0,1
# count = 0

# if nTerms <= 0:
#     print('Please enter a positive number')

# elif nTerms == 1:
#     print(n1)

# else:
#     while count < nTerms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1        

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1  
    else:
        return fibo(n-2)+fibo(n-1)

print(fibo(6)) 

def reverse(array):
    for i in range(0, int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

print(reverse([5,7,57,9,67]))        
