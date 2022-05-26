t=int(input())
for i in range(t):
    n,x,y=map(int, input().split())
    a=list(map(int, input().split()))
    sum=0
    for j in a:
        sum=sum+j
    sum2=0
    for k in a:
        if k-y>0:
            sum2=sum2+k-y
    if sum>sum2+x:
        print("COUPON")
    else:
        print("NO COUPON")
        
    