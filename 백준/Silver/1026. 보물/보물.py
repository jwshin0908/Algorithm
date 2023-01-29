import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

# pop을 통해서 지정된 위치 값 요소 삭제하고 리스트 변경
sum = 0
for i in range(n):
    sum+=min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(sum)