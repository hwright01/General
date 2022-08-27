def factor_list(n):
    factors = [{0}, {1}]
    num = 1
    while num < n:
        i = int(num/2)
        factors.append({1})
        while i >= num ** 0.5:
            if num % i == 0 and i not in factors[num]:
                facs = set(factors[i])
                facs.update({i, int(num/i)})
                try:
                    facs.remove(num)
                except:
                    pass
                factors[num].update(facs)
            i = i - 1
        num = num + 1
    return factors

a = factor_list(10000)[100]
print(a)