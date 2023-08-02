def power(x,n):
    assert int(n) == n, 'exponent must be integer'
    if n == 0:
        return 1
    elif n <0:
        return 1/x * power(x, n-1)
    else:
        return x * power(x, n-1)

print(power(2,4))     

base = int(input('pick a base'))
exp = int(input('pick a exponent'))
result = 1
while exp != 0:
    result *= base
    exp -= 1

print(str(result))    