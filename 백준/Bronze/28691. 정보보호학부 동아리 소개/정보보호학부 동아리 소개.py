import sys
input = sys.stdin.readline

word = input().rstrip()
club = {'M':'MatKor',
        'W':'WiCys',
        'C':'CyKor',
        'A':'AlKor',
        '$':'$clear'}

print(club[word])