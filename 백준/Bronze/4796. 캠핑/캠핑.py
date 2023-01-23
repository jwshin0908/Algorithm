# result : V//P * L + alpha(=min(V%P,L))
n=1
while True:
    L, P, V = map(int, input().split())
    if L==P==V==0:
        break
    result = (V//P)*L + min(V%P, L)
    print(f"Case {n}: {result}")
    n+=1