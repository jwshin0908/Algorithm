import sys
input = sys.stdin.readline

def area_1(x, y, W, H, X, Y):
    R = H // 2
    area1 = (x - X) ** 2 + (y - (Y + R)) ** 2
    if area1 <= R ** 2:
        return 1
    else:
        return 0
    
def area_2(x, y, W, H, X, Y):
    R = H // 2
    area2 = (x - (X + W)) ** 2 + (y - (Y + R)) ** 2
    if area2 <= R ** 2:
        return 1
    else:
        return 0

def area_3(x, y, W, H, X, Y):
    if (X <= x <= X + W) and (Y <= y <= Y + H):
        return 1
    else:
        return 0

W, H, X, Y, P = map(int, input().rstrip().split())
cnt = 0

for _ in range(P):
    result = []
    x, y = map(int, input().rstrip().split())
    result.append(area_1(x, y, W, H, X, Y))
    result.append(area_2(x, y, W, H, X, Y))
    result.append(area_3(x, y, W, H, X, Y))
    if 1 in result:
        cnt += 1

print(cnt)