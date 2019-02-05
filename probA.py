import sys

n,a,b=map(int,sys.stdin.readline().split())

print(min(a,b), end=" ")
min = 0 if (n>=a+b) else abs(a+b-n)
print(min)