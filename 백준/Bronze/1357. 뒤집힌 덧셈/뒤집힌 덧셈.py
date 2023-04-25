import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

def rev(n):
    nums = list(str(n))
    nums.reverse()
    a = ''.join(map(str, nums))
    return int(a)

result = rev(x) + rev(y)
print(rev(result))