def main():
    input()
    count = 0
    groups = input().split()
    counts = [groups.count(i) for i in ['1', '2', '3', '4']]

    count = count + counts[1] // 2 + counts[3]
    counts[1] = counts[1] % 2

    count = count + min(counts[2], counts[0])
    counts[2] = counts[2] - min(counts[2], counts[0])
    counts[0] = counts[0] - min(counts[2], counts[0])
    return count + -((counts[0] + 2*counts[1]) // -4) + counts[2]


if __name__ == "__main__":
    print(main())
