def main():
    [n, m, a] = [int(x) for x in input().split()]
    return (n // -a)*(m // -a)


if __name__ == "__main__":
    print(main())
