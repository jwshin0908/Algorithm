# 풀이 참고
# https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline

n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

# 결과 저장용 DP 테이블(각 원소별 이어진 수열 크기를 담기)
d = [1] * 1000

# DP(Bottom-Up)
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))