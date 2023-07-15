import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [input().rstrip() for _ in range(n)]
k = 1

while True:
    num_set = set([i[-k:] for i in nums])
    if len(num_set) == n:
        print(k)
        break
    else:
        k += 1