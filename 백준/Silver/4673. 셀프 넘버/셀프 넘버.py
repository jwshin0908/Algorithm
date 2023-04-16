def func1(n):
    a = list(str(n))
    a_sum = sum([int(i) for i in a])
    return n + a_sum

not_self_num = [func1(i) for i in range(1, 10001)]

for i in range(1, 10001):
    if i not in not_self_num:
        print(i)