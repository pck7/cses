n = int(input())
summ = n*(n+1)//2
if summ%2!=0:
    print('NO')
else:
    print('YES')
    arr_1= []
    arr_2 = []
    target = summ//2
    for x in range(n,0,-1):
        if x<=target:
            target-=x
            arr_1.append(x)
        else:
            arr_2.append(x)
    print(len(arr_1))
    print(*arr_1)
    print(len(arr_2))
    print(*arr_2)
