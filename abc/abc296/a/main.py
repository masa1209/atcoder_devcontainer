N = int(input())
S = list(input())
cnt = 0
for i in range(N):
    if i == 0:
        if S[i] == "M":
            cnt = 0
        else:
            cnt = 1
    if S[i] == "M" and i != 0:
        if cnt == 0:
            print("No")
            exit()
        else:
            cnt = 0
    elif S[i] == "F" and i != 0:
        if cnt == 1:
            print("No")
            exit()
        else:
            cnt = 1

print("Yes")
            
            
        