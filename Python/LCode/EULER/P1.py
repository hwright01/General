def res_sum(nums, max_num):
    total = 0
    for num in range(1, max_num):
        if any([num % x == 0 for x in nums]):
            total = total + num
    return total


print(res_sum([3, 5], 1000))
