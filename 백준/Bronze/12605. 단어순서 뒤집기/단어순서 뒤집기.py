import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    sentence = list(sys.stdin.readline().rstrip().split())
    sentence = sentence[::-1]
    print(f'Case #{i}: {" ".join(sentence)}')