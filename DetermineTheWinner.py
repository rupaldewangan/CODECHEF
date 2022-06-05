t=int(input())
for i in range(t):
    pa,pb,qa,qb=map(int, input().split())
    pm=max(pa,pb)
    qm=max(qa,qb)
    if pm==qm:
        print("TIE")
    elif pm>qm:
        print("Q")
    else:
        print("P")