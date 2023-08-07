import sys
input = sys.stdin.readline

K = int(input().rstrip())
width = []
height = []
total = []
for _ in range(6):
    a, b = map(int, input().rstrip().split())
    total.append(b)
    if (a == 1) or (a == 2):
        width.append(b)
    else:
        height.append(b)

max_width_index = total.index(max(width))
max_height_index = total.index(max(height))

small_width = abs(total[max_width_index - 1] - total[0 if max_width_index == 5 else max_width_index + 1])
small_height = abs(total[max_height_index - 1] - total[0 if max_height_index == 5 else max_height_index + 1])

area_1 = max(width) * max(height)
area_2 = small_width * small_height

print(K * (area_1 - area_2))