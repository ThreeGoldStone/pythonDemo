a = 10
b = 20
c = 1

if a > b:
    if c > a:
        print(c, a, b)
    elif c > b:
        print(a, c, b)
    else:
        print(a, b, c)
else:
    if c > b:
        print(c, b, a)
    elif c > a:
        print(b, c, a)
    else:
        print(b, a, c)
