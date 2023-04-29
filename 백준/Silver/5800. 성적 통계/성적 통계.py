import sys
input = sys.stdin.readline

k = int(input().rstrip())

for i in range(k):
    array = list(map(int, input().rstrip().split()))
    people = array[0]
    grade = array[1:]
    grade.sort(reverse=True)
    gap = []
    for j in range(people - 1):
        gap.append(grade[j] - grade[j + 1])

    print(f"Class {i+1}")
    print(f"Max {max(grade)}, Min {min(grade)}, Largest gap {max(gap)}")
