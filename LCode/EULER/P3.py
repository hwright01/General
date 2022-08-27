def addprimelist(p):
    p = [2] if p == [] else p
    i = p[-1]
    while True:
        if not any([i % x == 0 for x in p]):
            p.append(i)
            return(p)
        i = i + 1
    

def largestfactor(n):
    p = [2]
    pfactors = []
    i = 0
    while True:
        if n % p[i] == 0:
            pfactors.append(p[i])
            if max(pfactors) >= n:
                return int(max(pfactors))
            n = n / p[i]
            i = -1
        i = i + 1
        if n in p:
            return int(n)
        if i == len(p):
            if max(p) > n ** 0.5:
                return int(n)
            p = addprimelist(p)

print(largestfactor(11111111111))
