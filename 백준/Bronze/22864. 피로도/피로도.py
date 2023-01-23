# 작업 : 피로도 +A, 일+B / 휴식 : 피로도 -C
# 0<=피로도<=M

A, B, C, M = map(int, input().split())

tired = 0
work = 0

for i in range(24):
    if tired + A <=M:
        tired+=A
        work+=B
    else:
        if tired - C >=0:
            tired-=C
        else:
            tired=0

print(work)