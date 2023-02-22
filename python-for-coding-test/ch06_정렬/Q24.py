# Q24. 안테나(p.360)

n = int(input())
loc = list(map(int, input().split()))

loc.sort()

# median 위치에 설치
print(loc[(n-1)//2])