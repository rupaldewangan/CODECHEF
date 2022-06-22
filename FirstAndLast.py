t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    if n==2:
        print(a[0]+a[1])
    else:
                      
        print(a[0]+a[len(a)-1])   