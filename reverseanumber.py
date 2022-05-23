t=int(input())
for i in range(t):
    n=int(input())
    num=0
    while n!=0:
        r=n%10
        num=num*10 + r
        n=int(n/10)
    print(num)
