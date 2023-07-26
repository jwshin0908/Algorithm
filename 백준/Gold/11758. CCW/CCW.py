# CCW 알고리즘(외적)
# |x1 x2 x3 x1|
# |y1 y2 y3 y1|
# 반시계(+), 시계(-), 일직선(0)
import sys
input = sys.stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)