t=int(input())
for i in range(t):
    n,x=map(int, input().split())
    if n<=1:
        print(x)
    else:
        for i in range(n-1):
            x=x+x
        print(x)