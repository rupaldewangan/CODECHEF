t=int(input())
for i in range(t):
    n,a,b,c=map(int, input().split())
    if b>=n:
        if a>=(b-1) and c>=(b-1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")