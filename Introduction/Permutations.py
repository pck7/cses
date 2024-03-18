n = int(input())

if n==2 or n==3:
    print('NO SOLUTION')
  
elif n==4:
    print(*[2,4,1,3])
  
else:
    arr1 = [x for x in range(1,n+1,2)]
    arr2 = [x for x in range(2,n+1,2)]
    print(*arr1+arr2)
