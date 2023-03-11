N, P, Q, R, S = map(int, input().split())
A = input().split()

tmp_list = list()
tmp_list = A[P-1:Q]
tmp_list2 = list()
tmp_list2 = A[R-1:S]

#print(tmp_list)

A[R-1:S] = tmp_list
A[P-1:Q] = tmp_list2

print(*A)