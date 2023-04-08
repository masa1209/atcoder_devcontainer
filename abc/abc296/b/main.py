masu = []
y = 100
x = 100
for i in range(8):
    tmp = list(input())
    #print(tmp)
    if "*" in tmp:
        y = i
        for j in range(8):
            if "*" == tmp[j]:
                x = j
        break

a_x = ["a","b", "c", "d", "e", "f", "g", "h"]
a_y = ["8", "7", "6","5","4","3","2","1"] 

ans = "{}{}".format(a_x[x],a_y[y])

print(ans)
