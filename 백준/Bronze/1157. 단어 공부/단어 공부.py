# numpy없이 list unique 값을 위해 list(set(리스트)) 수행

s = str(input())
s = s.upper()
s_list = list(s)
s_list.sort()

alpha = []
digit = []
unique = list(set(s_list))

for i in unique:
    alpha.append(i)
    digit.append(s_list.count(i))

value = max(digit)

if digit.count(value) >= 2:
    print('?')
else:
    print(alpha[digit.index(value)])
