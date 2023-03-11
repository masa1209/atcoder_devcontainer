N, Q = map(int, input().split())

list = [0]*N

for i in range(Q):
    mes, target = map(int, input().split())
    if mes == 1:
        list[target-1] += 1
    elif mes == 2:
        list[target-1] += 2
    else:
        if list[target-1] >= 2:
            print("Yes")
        else:
            print("No")
