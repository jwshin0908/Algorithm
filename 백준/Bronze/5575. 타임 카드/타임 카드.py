import sys
input = sys.stdin.readline

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().rstrip().split())
    result = 3600 * (h2 - h1) + 60 * (m2 - m1) + (s2 - s1)
    hour = result // 3600
    minute = (result % 3600) // 60
    second = (result % 3600) % 60
    print(hour, minute, second)