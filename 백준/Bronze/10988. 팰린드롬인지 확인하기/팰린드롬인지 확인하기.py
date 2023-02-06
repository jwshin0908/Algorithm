import sys
s = sys.stdin.readline().rstrip()
cnt = 0
length = len(s)
for i in range(length):
    if s[i]!=s[length-1-i]:
        cnt+=1
if cnt==0:
    print(1)
else:
    print(0)