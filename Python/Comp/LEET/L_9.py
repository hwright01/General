def isPalindrome(x: int) -> bool:
    if x >= 0:
        return int(str(x)[::-1]) == x
    return False


print(isPalindrome(12321))
