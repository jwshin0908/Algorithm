import sys
input = sys.stdin.readline

n = int(input().rstrip())
tree = []
array = []

for _ in range(n):
    tree.append(int(input().rstrip()))

for i in range(1, n):
    array.append(tree[i] - tree[i - 1])

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

g = array[0]
for j in range(1, len(array)):
    g = gcd(g, array[j])

result = 0
for k in array:
    result += (k // g - 1)

print(result)