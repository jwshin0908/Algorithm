# Q08. 문자열 재정렬(p.322)
# isalpha() : 알파벳 or 한글인지 확인
# isdigit() : 숫자인지 확인
# isalnum() : 알파벳(한글) or 숫자인지 확인

s = list(str(input()))
string = []
digit = []

for i in s:
  if i.isalpha():
    string.append(i)
  else:
    digit.append(i)

string.sort()
sum = 0

for j in digit:
  sum += int(j)

print("".join(map(str, string)) + str(sum))