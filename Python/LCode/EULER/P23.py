from functions import factor_list, twosum

facs = [sum(x) for x in factor_list(28123)]
abundants = []
for ind, value in enumerate(facs):
    if value > ind:
        abundants.append(ind)


result = 0
for target in range(28125):
    if not twosum(abundants, target):
        if 0.5*target not in abundants:
            result += target
print(result)
