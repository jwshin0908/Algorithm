# 계수 정렬 문제
import sys
n = int(sys.stdin.readline().rstrip())

# 수가 10000보다 작거나 같은 자연수이므로 max는 10000으로 가정
count = [0] * 10001

# 입력 개수만큼 반복문을 돌리며 count 해당 값에 1 추가
for i in range(n):
    array = int(sys.stdin.readline().rstrip())
    count[array]+=1

# count 내에 반복문을 돌리며 해당 횟수만큼 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i)