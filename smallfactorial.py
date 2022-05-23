t=int(input())
for i in range(t):
    n=int(input())
    fact=1
    for j in range(n,1,-1):
        fact=fact*j
    print(fact)