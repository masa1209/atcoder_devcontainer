H, W = map(int, input().split())

import numpy as np

S = []
for i in range(H):
    s_r = list(input())
    S.append(s_r)

arr = np.array(S).T.tolist()
sort_s = sorted(arr)


T = []
for i in range(H):
    t_r = list(input())
    T.append(t_r)

arr = np.array(T).T.tolist()
sort_t = sorted(arr)


for i in range(W):
    if sort_s[i] != sort_t[i]:
        print("No")
        exit()
    else:
        continue
print("Yes")

