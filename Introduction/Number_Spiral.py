for _ in range(int(input())):
    y,x = map(int,input().split())
    if y>x:
        print([(y-1)**2 + x,y**2 - x + 1][y%2==0])
    else:
        print([(x-1)**2 + y,x**2 - y + 1][x%2!=0])
