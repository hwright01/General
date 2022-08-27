def addprimelist(n):
    p = [2]
    i = 3
    while i < n:
        if not any([i % x == 0 for x in p]):
            p.append(i)
        i = i + 1
    return sum(p)

print(addprimelist(2000000))