def main():
    vector = [0, 0, 0]
    for i in range(int(input())):
        vector = [sum(x) for x in zip(vector, [int(x) for x in input().split()])]
    return 'YES' if vector == [0, 0, 0] else 'NO'

if __name__ == "__main__":
    print(main())
