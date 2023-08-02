def dtb(n):
    assert int(n) == n, 'The parameter must be the integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10*dtb(int(n/2))

print(dtb(13))           