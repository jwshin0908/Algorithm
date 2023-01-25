N = int(input())
cnt = 0
new = N

while True:
    sum = new // 10 + new % 10
    new = 10 * (new % 10) + sum % 10
    cnt += 1
    if new == N:
        break
        
print(cnt)