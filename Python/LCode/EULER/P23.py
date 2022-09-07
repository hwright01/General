from functions import factor_list

facs = [sum(x) for x in factor_list(28123)]
abundants = []
for ind, value in enumerate(facs):
    if value > ind:
        abundants.append(ind)

for target in range(28123):
    lookup = {}
    for pos, number in enumerate(nums):
        if target - number in lookup:
            break
        else:
            lookup[number] = pos
