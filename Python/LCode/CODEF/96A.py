def main():
    num = input()
    return ('YES' if '1' * 7 in num or '0' * 7 in num else 'NO')

if __name__ == "__main__":
    print(main())
