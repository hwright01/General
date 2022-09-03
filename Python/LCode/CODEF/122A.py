def main():
    # Overkill for n<1000
    def lucky(n):
        base = [4, 7]
        if n == 1:
            return base, base
        total, prev = lucky(n-1)
        result = []
        for num in base:
            result = result + [int(str(num) + str(x)) for x in prev]
        return total + result, result

    almost = input()
    for num in lucky(len(almost))[0]:
        if int(almost) % num == 0:
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    print(main())
