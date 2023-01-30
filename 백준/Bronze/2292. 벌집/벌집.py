# 3n^2+3n+1 구현 -> 출력 초과 error
n = int(input())

nums_cum = 1  # 벌집의 개수, 1부터 시작
cnt = 1
while n>nums_cum:
    nums_cum+=6*cnt  # 벌집이 6의 배수로 증가(6,12,18,...)
    cnt+=1  # 반복문을 반복하는 횟수
print(cnt)