def main():
    given = input()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for vowel in vowels:
        given = given.replace(vowel, '')
    given = [(x.swapcase() if x.isupper() else x) for x in given]
    given = '.'.join(given)
    return ''.join(['.', given])


if __name__ == "__main__":
    print(main())
