import sys

def rlsi(): return [int(x) for x in sys.stdin.readline().split()]

n,m = map(int,sys.stdin.readline().split())
xlist = rlsi()
sides_list = [[] for i in range(m)]
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    sides_list[i] = [a-1,b-1,c]

sides_list = sorted(sides_list, key=lambda x: x[2])
# 解答みても理解できず、解説サイトや、他者の解答をデバッグして、
# 動作のイメージをつかんだため、全てコメントアウト
# p = list(range(n))
# r,bad = [0] * n, [0] * n
# wt = xlist[:]

# def find(a):
#     if p[a] != a:
#         p[a] = find(p[a])
#     return p[a]

# def union(a,b,c):
#     a,b = find(a),find(b)
#     if r[a] < r[b]: a, b = b, a
#     p[b] = a
#     r[a] += r[a] == r[b]
#     wt[a] += wt[b]
#     bad[a] += bad[b]
#     if wt[a] < c:
#         bad[a] += 1
#     else:
#         bad[a] = 0

# def add(a,c):
#     a = find(a)
#     if wt[a] < c:
#         bad[a] += 1

# for a,b,c in sides_list:
#     if find(a) == find(b):
#         add(a,c)
#     else:
#         union(a,b,c)

# ans=0
# for u in range(0, n):
#     if p[u] == u: ans += bad[u]

# print(ans)