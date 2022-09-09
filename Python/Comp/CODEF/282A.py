def main():
    count = 0
    for i in range(int(input())):
        num = input()
        count = count + num.count('+') - num.count('-')
    return int(count / 2)


if __name__ == "__main__":
    print(main())
