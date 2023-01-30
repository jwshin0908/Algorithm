import sys
c = int(sys.stdin.readline().rstrip())
for i in range(c):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    num = a[0]
    score = a[1:]
    mean = sum(score)/num
    cnt = [i for i in score if i > mean]
    print(f"{100*len(cnt)/num:.3f}%")