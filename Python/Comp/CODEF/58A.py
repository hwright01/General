def main():
    message = input()
    count = 0
    word = [x for x in 'hello']
    for index, value in enumerate(message):
        if value == word[count]:
            count = count + 1
            if count == len(word):
                return 'YES'
    return 'NO'


if __name__ == "__main__":
    print(main())
