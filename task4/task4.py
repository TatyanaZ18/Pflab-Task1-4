import sys

array_txt = sys.argv[1]
file = open(array_txt, "r") #array.txt
arr = file.readlines()
for i in range(0, len(arr)):
    arr[i] = arr[i].rstrip()
    arr[i] = int(arr[i])
arr.sort()
median = len(arr) // 2
count = 0
for i in range(0, len(arr)):
    count += abs(arr[i] - arr[median])

print(count)

