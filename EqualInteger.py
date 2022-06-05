t=int(input())
for i in range(t):
    x,y=map(int, input().split())
    count=0
    if x>y:
        while x>y:
            count=count+1
            y=y+2
    elif y>x:
        while y>x:
            count=count+1
            x=x+1
    print(count)
            