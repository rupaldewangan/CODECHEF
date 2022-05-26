T=int(input())
count=0
for i in range(T):
    x,y=map(int, input().split())
    while y>x:
        x=x+8
        count=count+1
    print(count)
    
    