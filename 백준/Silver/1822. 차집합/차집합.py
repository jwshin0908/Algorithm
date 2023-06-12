# list 사용 시 시간 초과 -> set 사용
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))

result = sorted(A - B)

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(' '.join(map(str, result)))