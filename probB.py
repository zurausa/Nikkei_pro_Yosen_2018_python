import sys
 
n=int(sys.stdin.readline())
a=sys.stdin.readline()
b=sys.stdin.readline()
c=sys.stdin.readline()
 
 
cnt = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        continue
    elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
        cnt = cnt + 1
    else:
        cnt = cnt + 2
print(cnt)