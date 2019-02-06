# union-find の練習コード
# https://atc001.contest.atcoder.jp/tasks/unionfind_a
import sys

def rlsi(): return [int(x) for x in sys.stdin.readline().split()]

n,m = map(int, sys.stdin.readline().split())
x = [[] for i in range(m)]
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    x[i] = [a,b-1,c-1]

p = list(range(n))
r = [0] * n

# 親ノードの確認
# setでやらないのは群が二つ以上の可能性もあるため、考慮できない
def find(x):
    if p[x] != x:
        p[x] == find(p[x])
    return p[x]

#  ノードの連結
# 子の数(r[i])を確認して、どちらが親かを決める
# 同数の場合は適当に決定
def union(x,y):
    x,y = find(x),find(y)
    if r[y] > r[x]: x,y = y,x
    p[y] = x
    r[x] += r[x] == r[y]

def conf(x,y):
    x,y = find(x),find(y)
    if x == y:
        print('Yes')
    else:
        print('No')

for a,b,c in x:
    if a == 0 and find(b) != find(c):
        union(b,c)
    elif a == 1:
        conf(b,c)