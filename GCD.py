def gcd(x,y):
    assert int(x) == x and int(y) == y, 'The numbers must be integers'
    if x<0:
        x = -1*x
    if y<0:
        y = -1*y    
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

print(gcd(16,96))     

def computeGCD(a,b):
    if a>b:
        small = b
    if a<b:
        small = a

    for i in range(1, small+1):
        if((a%i == 0) and (b%i == 0)):
            gcd = i

    return gcd


print("the gcd of 60 and 48 is: ", end="")
print(computeGCD(60,48))                
            

