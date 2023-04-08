N, X = map(int, input().split())

A = set(map(int, input().split()))
#print(A)
# num_set = set()
# def check_sum(nums, X):
#     n = len(nums)
#     memo = [[False] * (X + 1) for _ in range(n + 1)]
    
#     # 動的計画法による組み合わせの探索
#     for i in range(n + 1):
#         memo[i][0] = True
#     for i in range(1, n + 1):
#         for j in range(1, X + 1):
#             memo[i][j] = memo[i - 1][j]
#             if j - nums[i - 1] >= 0:
#                 memo[i][j] = memo[i][j] or memo[i - 1][j - nums[i - 1]]
    
#     return memo[n][X]

for i in A:
    if X == 0:
        print("Yes")
        exit()
    elif X+i in A:
        print("Yes")
        exit()

print("No")


