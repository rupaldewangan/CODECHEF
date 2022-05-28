t=int(intput())
for i in range(t):
    n=int(input())
    step=1:
    move=0
    while True:
        if n>=step+3:
            step=step+3
            move=move+1
            if n==step:
                break
        elif n>=step+2:
            step=step+2
            move=move+1
            if n==step:
                break
        elif n>=step+1:
            step=step+1
            move=move+1
            if n==step:
                break