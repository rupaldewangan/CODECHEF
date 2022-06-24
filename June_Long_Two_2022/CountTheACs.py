t= int(input())
for i in range(t):
    p=int(input())
    if p>100:
        if p//100>0:
            if(p//100+p%100)<=10:
                print(p//100 + p%100)
            else:
                print(-1)
    elif p>=0 and p<=10:
        print(p)
    else:
        print(-1)