n = int(input())
res = [n]
while n!=1:
    n = [n//2,3*n+1][n%2!=0]
    res.append(n)
print(*res)
