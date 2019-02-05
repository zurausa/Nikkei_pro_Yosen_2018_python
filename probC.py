import sys
from collections import deque


n=int(sys.stdin.readline())
M = deque(maxlen=n)
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    M.append([a,b])

M = sorted(M,key=lambda x:sum(x))
cnt = 0
for i in range(n):
    if i%2==0:
        cnt += M.pop()[0]
    else:
        cnt -= M.pop()[1]
print(cnt)
