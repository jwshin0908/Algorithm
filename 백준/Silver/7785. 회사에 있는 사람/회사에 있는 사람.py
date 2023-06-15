import sys
input = sys.stdin.readline

n = int(input().rstrip())
company = dict()

for _ in range(n):
    a, b = input().rstrip().split()
    company[a] = b

result = [k for k, v in company.items() if v == 'enter']
result.sort(reverse=True)

for i in result:
    print(i)