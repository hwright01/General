def main():
    input()
    count = 1
    coins = sorted([int(x) for x in input().split()])
    while sum(coins[-count:]) <= sum(coins) / 2:
        count = count + 1
    return count

if __name__ == "__main__":
    print(main())
