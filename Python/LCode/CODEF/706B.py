def binary_search(arr, num):
    total = 0
    if len(arr) <= 2:
        return sum([int(num >= x) for x in arr])
    mid = len(arr) // 2
    if arr[mid] == num:
        i = 1
        while arr[mid+i] == num:
            i = i + 1
        return mid + i
    elif arr[mid] < num:
        return mid + 1 + binary_search(arr[mid+1:], num)
    else:
        return binary_search(arr[:mid], num)


input()
shops = sorted([int(x) for x in input().split()])
out = []

for i in range(int(input())):
    out.append(int(input()))

for num in out:
    print(binary_search(shops, num))
