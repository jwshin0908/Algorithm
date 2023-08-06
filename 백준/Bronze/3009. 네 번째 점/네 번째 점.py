import sys

dict_a = {}
dict_b = {}

for _ in range(3):
    a, b = map(int, input().rstrip().split())
    if a not in dict_a.keys():
        dict_a[a] = 1
    else:
        dict_a[a] += 1
    
    if b not in dict_b.keys():
        dict_b[b] = 1
    else:
        dict_b[b] += 1

for key in dict_a.keys():
    if dict_a[key] == 1:
        result_a = key
for key in dict_b.keys():
    if dict_b[key] == 1:
        result_b = key
        
print(result_a, result_b)