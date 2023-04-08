S = list(input())

for  i in range(len(S)):
    if i%2 == 0: 
        tmp = S[i]
        S[i] = S[i+1]
        S[i+1] = tmp
        
print(*S, sep = "")