N = int(input())
S = list(input())

cnt = 0

for i in range(N):
    if S[i] == "n":
        cnt = 1
    elif S[i] == "a" and cnt == 1:
        S[i] = "ya"
        cnt = 0
    else:
        cnt = 0

print(*S, sep="")