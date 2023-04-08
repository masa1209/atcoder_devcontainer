import copy

H, W = map(int, input().split())
field = []
for i in range(H):
    field.append(list(map(int, input().split())))

def count(i, j, st, depth):
    
    #print("i:{},j:{}".format(i,j))
    if field[i][j] not in st:
        
        st.add(field[i][j])
    else:
        return 0
    
    if i == H-1 and j == W-1:
        print(st)
        st.remove(field[i][j])
        return 1
    #print(st)
    cnt = 0
    print(cnt)
    if i < H-1:
        #print("check:y")
        cnt += count(i+1, j, st, depth)
        print(cnt)
    if j < W-1:
        #print("check:x")
        cnt += count(i, j+1, st, depth)
        print(cnt)
    st.remove(field[i][j])
    print(cnt)
    return cnt

ans = count(0, 0, set(), 0)
print(ans)