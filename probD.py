import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split()) 
al,cnt=[[] for _ in range(n)],[0]*n
for i in range(n+m-1):
    a,b=map(int,sys.stdin.readline().split())
    al[a-1].append(b-1)
    cnt[b-1] += 1
ans = [0]*n
que = deque()

# children = []
# child = 0
# for i in range(n):
#     if len(children) == 0:        
#         children = set(cnf)-set(bl)
#         parent = child
 
#     child = children.pop()
    
#     j = 0
#     while j < len(al):
#         if al[j] == child:
#             al.pop(j)
#             bl.pop(j)
#         else:
#             j += 1
#     ans[child-1] = parent
#     cnf.remove(child)

for i in range(n):
    if  cnt[i] == 0:
        que.append(i)
        break

while que:
    p = que.popleft()
    
    for j in al[p]:
        cnt[j] -= 1
        if cnt[j] == 0:
            que.append(j)
            ans[j]=p + 1

for i in range(n):
    print(ans[i])