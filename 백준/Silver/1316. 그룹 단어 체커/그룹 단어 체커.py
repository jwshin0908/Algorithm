import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = n
for _ in range(n):
    x = input().rstrip()
    for i in range(0, len(x) - 1):
        # 다음 문자랑 같을 경우 : 통과
        if x[i] == x[i + 1]:
            pass
        # 다음 문자랑 다를 경우 : 남은 문자열 중에 존재하는지 확인
        elif x[i] in x[i + 1:]:
            cnt -= 1 # 존재할 경우 그룹 단어 아니므로 제외
            break
print(cnt)