from itertools import combinations

n, k = map(int, input().split())

# combinations(iterable, r) : 반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 반환하는 함수
# list로 변환 후 len 출력 시 조합 개수 도출 가능
print(len(list(combinations(range(n), k))))