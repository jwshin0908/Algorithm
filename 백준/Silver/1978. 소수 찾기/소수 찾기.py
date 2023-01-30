import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
prime = []

for i in nums:
    if i == 1:
        continue
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt==0:
        prime.append(i)
print(len(prime))