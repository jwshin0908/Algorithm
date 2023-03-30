import sys
input = sys.stdin.readline

n = int(input().rstrip())
meeting = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    meeting.append((a, b))

# 종료 시간을 오름차순으로 정렬, 이후 시작 시간 오름차순으로 정렬
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

now = 0
cnt = 0

# 현재 시간이 회의 시작시간보다 이르다면, 회의를 시작
for i in meeting:
  if now <= i[0]:
    cnt += 1
    now = i[1]

print(cnt)