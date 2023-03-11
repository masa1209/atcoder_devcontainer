N,W = map(int, input().split())

w = []
v = []
for i in range( N):
    w_tmp, v_tmp = map(int, input().split())
    w.append(w_tmp)
    v.append(v_tmp)

dp = [[0 for j in range(100010)]for i in range(110)]

for i in range(N):
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]
        if (j - w[i]) >= 0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]] + v[i])
            
print(dp[N-1][W])