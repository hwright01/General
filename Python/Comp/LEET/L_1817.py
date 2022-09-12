def findingUsersActiveMinutes(logs, k):
    new_logs, result = [], []
    for log in logs:
        if log not in new_logs:
            new_logs.append(log)
    for i in range(k):
        result.append(sum([int(x[0] == i) for x in new_logs]))
    return [result.count(x+1) for x in range(k)]


print(findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))
