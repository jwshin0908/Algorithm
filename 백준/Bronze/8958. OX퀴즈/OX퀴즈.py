t = int(input())
for _ in range(t):
    s = input()
    result = 0
    cum = 0
    for i in range(len(s)):
        if s[i]=='O':
            result+=1+cum
            if i==len(s)-1:
                break
            else:
                if s[i]==s[i+1]:
                    cum+=1
                else :
                    cum = 0
        else :
            cum = 0
    print(result)