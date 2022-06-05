t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    if n==2:
        print(a[0]+a[1])
    else:
        while True:
            if a[len-2]>a[len-1]:
                temp=a[0]
                a[0]=a[len-1]
                for i in range(1,len-1):
                    a[i+1]=a[i]
                a[i]=temp
            break
        print(a[0]+a[len-1])   