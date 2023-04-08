N, M = map(int, input().split())
b = 100000000000000000000
ans = 10000000000000000000
flag = 0
import math
for a in range(1,N+1):
    b = math.ceil(M/a)
    if b <= N:
        ans = min(ans, a*b)
        #print("{}:{}:{}".format(i, b, ans))
        flag = 1
    if a > b:
        break
if flag == 1:
    print(ans)
else:
    print(-1)
        