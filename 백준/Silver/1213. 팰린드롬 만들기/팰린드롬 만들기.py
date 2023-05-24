import sys
input = sys.stdin.readline

word = list(input().rstrip())
word_dict = {}
for i in word:
    if i in word_dict.keys():
        word_dict[i] += 1
    else:
        word_dict[i] = 1
word_dict = dict(sorted(word_dict.items()))
half = [k * (v // 2) for k, v in word_dict.items()]
odd = [k for k, v in word_dict.items() if v % 2 != 0]

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    result = half + odd + half[::-1]
    print("".join(map(str, result)))