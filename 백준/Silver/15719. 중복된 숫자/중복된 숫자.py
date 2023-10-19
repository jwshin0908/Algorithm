import sys
input = sys.stdin.readline

N = int(input().rstrip())
sum_N = sum(range(1, int(N)))

array = input().rstrip()
sum_array = 0
temp = ""

for i in array:
    if i.isdigit():
        temp += i
    else:
        sum_array += int(temp)
        temp = ""

sum_array += int(temp)

print(sum_array - sum_N)