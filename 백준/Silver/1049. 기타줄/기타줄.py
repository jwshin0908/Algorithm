import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
package = []
one = []

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    package.append(a)
    one.append(b)

package.sort()
one.sort()

# 6으로 나눠떨어지는 몫
def share(x):
    if package[0] >= one[0] * 6:
        return (x // 6) * one[0] * 6
    else:
        return (x // 6) * package[0]

# 6으로 나눈 나머지
def remain(x):
    if package[0] >= one[0] * (x % 6):
        return (x % 6) * one[0]
    else:
        return package[0]

result = share(n) + remain(n)
print(result)