t=int(input())
for i in range(t):
    n=int(input())
    k=list(map(int, input().split()))
    for i in range(0,len(k)):
        if i!=len(k)-1:
            if k[i]>k[i+1]:
                print("No")
                break
    else:
        print("Yes") 