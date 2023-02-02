while True:
    s = input()
    length = len(s)
    cnt = 0
    if s=='0':
        break
    for i in range(int(length//2)):
        if s[i]!=s[length-i-1]:
            cnt+=1
    if cnt==0:
        print('yes')
    else:
        print('no')
