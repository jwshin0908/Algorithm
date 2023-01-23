# min(컵홀더 개수, 사람 수)
n = int(input())
s = str(input())

s = s.replace("S","*S*")
s = s.replace("LL","*LL*")
s = s.replace("**","*")

num = s.count("*")
result = min(num, n)

print(result)