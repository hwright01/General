def main():
    input()
    return " ".join(str(y) for y in sorted([int(x) for x in input().split()]))

if __name__ == "__main__":
    print(main())
