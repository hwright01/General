def longest_prefix(strs):
    longest = ''
    for i in range(min([len(x) for x in strs])):
        if [x[i] for x in strs].count(strs[0][i]) != len(strs):
            return strs[0][0:i] if i != 0 else ''
    return min(strs, key=len)
