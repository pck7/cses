n = int(input())
arr = [int(x) for x in input().split()]
count = 0
for x in range(n-1):
    if arr[x]>arr[x+1]:
        count += arr[x]-arr[x+1]
        arr[x+1] = arr[x]
print(count)
