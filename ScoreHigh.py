T=int(input())
for i in range(T):
    N=int(input())
    Na,Nb,Nc,Nd = map(int, input().split())
    if N==(Na+Nb+Nc+Nd):
        if Na>Nb and Na>Nc and Na>Nd:
            max=Na
        elif Nb>Na and Nb>Nc and Nb>Nd:
            max=Nb
        elif Nc>Nb and Nc>Na and Nc>Nd:
            max=Nc
        else:
            max=Nd
        print(max)