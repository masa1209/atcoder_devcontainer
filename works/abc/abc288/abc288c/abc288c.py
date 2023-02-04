n, m = map(int, input().split())
p = [-1] * (n + 1)

def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]

def unite(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  p[y] = x

result = 0
for i in range(m):
    a, b = map(int, input().split())
    if root(a) != root(b):
        unite(a, b)
    else:
       result += 1

print(result)