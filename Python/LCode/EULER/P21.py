def factor_list_max(n):
    factors = [{0}, {1}]
    num = 1
    redo = True
    while num < n:
        i = int(num/2)
        factors.append({1})
        while i >= num ** 0.5:
            if num % i == 0:
                facs = set(factors[i])
                facs.update({i, int(num/i)})
                try:
                    facs.remove(num)
                except Exception:
                    pass
                factors[num].update(facs)
            i = i - 1
        num = num + 1
        if num == n and redo:
            n = max([sum(x) for x in factors])
            redo = False
    return factors


def amicable(n):
    result = []
    sums = [sum(x) for x in factor_list_max(n)]
    for ind, sumval in enumerate(sums):
        if ind >= n:
            return set(result)
        if sums[sumval] == ind and sumval != ind:
            if sumval >= n:
                result.append(ind)
            else:
                result = result + [sumval, ind]


print(sum(amicable(10000)))
