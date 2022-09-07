from tkinter import N


def main():
    [n, k] = [int(x) for x in input().split()]
    return 2*k - 1 if k <= int((n+1)*0.5) else 2*(k-int((n+1)*0.5))


if __name__ == "__main__":
    print(main())
