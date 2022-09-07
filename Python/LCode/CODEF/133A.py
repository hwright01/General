def main():
    instructions = ['H', 'Q', '9']
    code = input()
    return 'YES' if any([x in code for x in instructions]) else 'NO'


if __name__ == "__main__":
    print(main())
