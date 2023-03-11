N= int(input())

a, b, c = [0]*N, [0]*N, [0]*N

a[0], b[0], c[0] = map(int, input().split())
for i in range(1,N):
    p,q,r = map(int, input().split())
    a[i] = p + max(b[i-1], c[i-1])
    b[i] = q + max(a[i-1], c[i-1])
    c[i] = r + max(a[i-1], b[i-1])


print(max(a[N-1], b[N-1], c[N-1]))