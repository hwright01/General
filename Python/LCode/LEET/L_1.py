def twoSum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for pos, number in enumerate(nums):
        if target - number in lookup:
            return lookup[target-number], pos
        else:
            lookup[number] = pos


print(twoSum([2, 3, 4], target=6))
