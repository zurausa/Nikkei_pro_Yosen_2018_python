import sys

n=int(sys.stdin.readline())
a=list(sys.stdin.readline())
b=list(sys.stdin.readline())
c=list(sys.stdin.readline())

cnt = 0
for i in range(n):
    cnt += len(set([a[i],b[i],c[i]]))-1
print(cnt)
