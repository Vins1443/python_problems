def sum(n):
    assert n>=0 and int(n) == n, 'The number must be a positive integer only'
    if n == 0:
        return 0
    else:
        return sum(int(n/10))+int(n%10)

print(sum(54))   
print(sum(276))         
