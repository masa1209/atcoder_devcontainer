N, M = map(int, input().split())

visited = [False] * N
ans = 0

w = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    w[u-1].append(v-1)
    w[v-1].append(u-1)


def dfs(i):
    visited[i] = True
    for j in w[i]:
        if not visited[j]:
            dfs(j)
        
for i in range(N):
    if not visited[i]:
        ans += 1
        dfs(i)
        
print(ans)
# def dfs(i):
#     visited[i] = True
#     for j in w[i]:
#         if not visited[j]:
#             dfs(j)

# n, m = map(int, input().split())
# w = [[] for _ in range(n)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     w[u-1].append(v-1)
#     w[v-1].append(u-1)

# visited = [False] * n
# ans = 0
# for i in range(n):
#     if not visited[i]:
#         ans += 1
#         dfs(i)

# print(ans)