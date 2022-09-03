def main():
    n = int(input())
    result=0
    while(n > 0):
        if input().count('1') >= 2:
            result = result +1
        n = n - 1
    print(result)
        

if __name__ == "__main__":
    main()
