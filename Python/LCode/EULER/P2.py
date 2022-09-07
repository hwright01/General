def fibs(n):
    f = [1, 1, 2]
    i = 2
    while f[i] < n:
        f.append(f[i] + f[i-1])
        i = i + 1
    return f[1:-1]


print(sum([(x if x % 2 == 0 else 0) for x in fibs(4000000)]))
