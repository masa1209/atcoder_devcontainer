import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

seen = [False] * N

w = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    w[a].append(b)
    w[b].append(a)

def dfs(i):
    seen[i] = True
    for j in w[i]:
        if not seen[j]:
            dfs(j)

ans = 0

for i in range(N):
    if not seen[i]:
        ans += 1
        dfs(i)
    
    
print(M - N + ans)