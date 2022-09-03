import numpy as np

# Shit code

def palindromes(n):
    result=[]
    for num in range(10 ** (n-1), 10 ** n):
        result.append(int(str(num) + str(num)[::-1]))
        result.append(int(str(num) + str(num)[1::-1]))
    return result

def largestpalindrome(n):
    for nums in sorted(palindromes(n))[::-1]:
        for num in range(10 ** (n-1), 10 ** n):
            if nums % num == 0 and 10 ** (n-1) < nums / num < 10 ** n:
                return nums

print(largestpalindrome(3))
