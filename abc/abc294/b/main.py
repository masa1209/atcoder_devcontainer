H, W = map(int, input().split())
alpha = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(H):
    ans_list = []
    A = list(map(int, input().split()))
    for j in A:
        if j == 0:
            ans_list.append(".")
        else:
            ans_list.append(alpha[j-1])
    print(*ans_list, sep="")