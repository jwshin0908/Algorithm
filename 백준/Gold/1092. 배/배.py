import sys
input = sys.stdin.readline

N = int(input().rstrip())
crane = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
box = list(map(int, input().rstrip().split()))
time = 0

crane.sort(reverse = True)
box.sort(reverse = True)

if crane[0] < box[0]:
    print(-1)
    sys.exit()

while len(box) > 0:
    for i in crane:
        for j in box:
            if i >= j:
                box.remove(j)
                break
    time += 1
            
print(time)