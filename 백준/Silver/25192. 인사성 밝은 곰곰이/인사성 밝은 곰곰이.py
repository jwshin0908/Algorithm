import sys
input = sys.stdin.readline

N = int(input().rstrip())
user = dict()
result = 0
for _ in range(N):
    word = input().rstrip()
    if word == 'ENTER':
        result += sum(user.values())
        user = dict()
    else:
        if word not in user:
            user[word] = 1
            
result += sum(user.values())
print(result)