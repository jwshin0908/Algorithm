import sys
n = int(sys.stdin.readline().rstrip())
r_list = []

for _ in range(n):
    r_list.append(int(sys.stdin.readline().rstrip()))
r_list.sort()

w = []
for i in r_list:
    w.append(i*n)
    n-=1
print(max(w))