import sys
input = sys.stdin.readline

word = input().rstrip()
cheer = {'SONGDO':'HIGHSCHOOL',
         'CODE':'MASTER',
         '2023':'0611',
         'ALGORITHM':'CONTEST'}

print(cheer[word])