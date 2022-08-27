file = open(r'C:\Users\villa\Documents\General\General\LCode\EULER\p022_names.txt', 'r')
names = sorted([x[1:-1] for x in file.readline().split(',')])
total = 0

for index, name in enumerate(names):
    total = total + (index + 1) * sum([ord(x) - 64 for x in name])

print(total)