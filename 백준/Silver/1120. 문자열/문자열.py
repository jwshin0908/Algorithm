import sys
input = sys.stdin.readline

A, B = input().rstrip().split()
result = []

for i in range(1 + len(B) - len(A)):
    B_temp = B[i:i + len(A)]
    cnt = 0
    for j in range(len(A)):
        if A[j] != B_temp[j]:
            cnt += 1
    result.append(cnt)
    
print(min(result))