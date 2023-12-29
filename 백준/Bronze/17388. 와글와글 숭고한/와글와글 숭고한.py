import sys
input = sys.stdin.readline

S, K, H = map(int, input().rstrip().split())
score = {'Soongsil' : S, 'Korea' : K, 'Hanyang' : H}

if (S + K + H) >= 100:
    print('OK')
else:
    for key, value in score.items():
        if min(score.values()) == value:
            print(key)