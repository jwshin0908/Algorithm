s = str(input())
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    s = s.replace(i, '1')

alpha, digit = 0, 0
sentence = list(s)

for j in sentence:
    if j.isalpha():
        alpha += 1
    else:
        digit += 1

print(alpha + digit)
