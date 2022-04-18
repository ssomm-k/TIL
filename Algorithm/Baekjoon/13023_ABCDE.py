def dfs(d):


N,M = map(int,input().split())

friend = [[] for _ in range(N)]
for i in range(M):
    f_1,f_2 = map(int,input().split())
    friend[f_1].append(f_2)
    friend[f_2].append(f_1)

visited = [0]*N