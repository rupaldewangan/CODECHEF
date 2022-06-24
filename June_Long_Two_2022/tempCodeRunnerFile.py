t=int(int(input))
for i in range(t):
    n=int(input())
    s=input()
    k=""
    for i in s:
        if i=="A":
            k=k+"T"
        elif i=="T":
            k=k+"A"
        elif i=="C":
            k=k+"G"
        elif i=="G":
            k=k+"C"
    print(k)