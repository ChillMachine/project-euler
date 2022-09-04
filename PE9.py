def PE9():
    for a in range(1,1001):
        for b in range(a+1,1001):
            c = (a**2+b**2)**0.5
            cTr = c == int(c)
            if a**2+b**2 == c**2 and a+b+c == 1000 and cTr:
                return int(a*b*c)
print(PE9())