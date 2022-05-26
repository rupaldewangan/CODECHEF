t=int(intput())
for i in range(t):
    n,s=map(int, input().split())
    if n>s:
        print(s)
    else:
        re = (2*n)-s
        print(re)   