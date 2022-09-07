def main():
    [n, k] = input().split()
    n, k = int(n), int(k) - 1
    count = k
    scores = input().split()
    if int(scores[k]) == 0:
        return (n-scores.count('0'))
    else:
        while int(scores[count]) == int(scores[k]):
            count = count + 1
            if count == n:
                return n
        return count


if __name__ == "__main__":
    print(main())
