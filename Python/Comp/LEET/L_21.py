def mergetwosorted(list1, list2):
    ind1 = 0
    result = []
    for _, value in enumerate(list1):
        while value > list2[ind1] and ind1 < len(list2):
            result.append(list2[ind1])
            ind1 += 1
        result.append(value)
    if ind1 != len(list2):
        return result + list2[ind1:]
    return result
