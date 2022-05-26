t=int(input())
for i in range(t):
    x,y=map(int, input().split())
    print(min(500-(x*2)+1000-((x+y)*4),1000-(y*4)+500-((x+y)*2)))
