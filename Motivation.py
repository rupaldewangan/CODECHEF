t=int(input())
for i in range(t):
    n,x=map(int,input().split(" "))
    l=[]
    for i in range(n):
        s,r=map(int,input().split(" "))
        if s<=x:
            l.append(r)
    print(max(l)) 