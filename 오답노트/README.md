# 💻코딩테스트 준비용 오답노트
## 목차
[1. 시뮬레이션](#1-시뮬레이션)<br/>
&emsp;[(1) dx dy technique](#1-dx-dy-technique)<br/>
&emsp;[(2) 객체](#2-객체)<br/>
&emsp;[(3) 일반 정렬](#3-일반-정렬)<br/>
&emsp;[(4) 객체 정렬](#4-객체-정렬)<br/>
&emsp;[(5) 격자 안에서 완전 탐색](#5-격자-안에서-완전-탐색)<br/>
&emsp;[(6) 격자 안에서 밀고 당기기](#6-격자-안에서-밀고-당기기)<br/>
&emsp;[(7) 격자 안에서 터지고 떨어지는 경우](#7-격자-안에서-터지고-떨어지는-경우)<br/>
&emsp;[(8) 격자 안에서 단일 객체를 이동](#8-격자-안에서-단일-객체를-이동)<br/>
&emsp;[(9) 격자 안에서 여러 객제를 이동](#9-격자-안에서-여러-객제를-이동)<br/>

[2. 백트래킹](#2-백트래킹)<br/>


# 1. 시뮬레이션
## (1) dx dy technique

<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3
N = int(input())
array = []
for _ in range(N):
    array.append(list(input()))
loc = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = (loc - 1) // N

if loc <= N:
    x = 0
    y = loc - 1
elif loc <= 2 * N:
    x = loc - N - 1
    y = N - 1
elif loc <= 3 * N:
    x = N - 1
    y = N - (loc - 2 * N)
elif loc <= 4 * N:
    x = N - (loc - 3 * N)
    y = 0

def in_range(x, y):
    return (0 <= x and x < N) and (0 <= y and y < N)

cnt = 1

while True:
    mirror = array[x][y]
    if mirror == '/':
        if (dir_num % 2 == 1):
            dir_num = (dir_num + 3) % 4
        else:
            dir_num = (dir_num + 1) % 4
    else:
        if (dir_num % 2 == 1):
            dir_num = (dir_num + 1) % 4
        else:
            dir_num = (dir_num + 3) % 4
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    if in_range(x, y) == False:
        break
    cnt += 1
    
print(cnt)
```
</div>
</details>


## (2) 객체

## (3) 일반 정렬

## (4) 객체 정렬

## (5) 격자 안에서 완전 탐색
**완전 탐색**
+ 문제를 해결할 수 있는 가장 naive한 방법
+ 시간복잡도를 계산해본 후 적용할 것
+ For문 기반 / 재귀함수 기반의 Backtracking(Brute Force) 기법

**오답 문제 1 : 행복한 수열의 개수**
+ 문제 상황
    + 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
    + n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램
    + 1 ≤ m ≤ n ≤ 100
+ 알고리즘 설계
    + 동일한 원소 개수 cnt = 1로 지정 / array 첫 번째 원소 = num으로 지정 후 다음 원소와 비교해가며 cnt & num 값 update
    + 원소 값이 동일하면 cnt를 더하고, 다르면 1로 초기화 / array 끝까지 도달했을 때 cnt가 m 이상일 경우 1을 반환
    + 각 열, 각 행마다 개수를 각각 도출해서 더하기로 결정
+ 틀린 이유
    + 함수 내에서 원소 값이 다르다고 cnt를 1로 초기화하면 안 
+ 수정
    + ```max_cnt = max(max_cnt, cnt)```을 통해 최대 cnt 값을 따로 저장해간 후 m 값과 비교하기
+ 느낀 점
    + 테스트케이스 이외의 다양한 반례 상황 찾아보기
<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def same_number(arr, n, m):
    max_cnt = 1
    cnt = 1
    num = arr[0]
    for i in range(1, n):
        if arr[i] == num:
            cnt += 1
        else:
            cnt = 1
        num = arr[i]
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        return 1
    else:
        return 0

result = 0

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(array[i][j])
    result += same_number(arr, n, m)


for j in range(n):
    arr = []
    for i in range(n):
        arr.append(array[i][j])
    result += same_number(arr, n, m)

print(result)
```
</div>
</details>


## (6) 격자 안에서 밀고 당기기

## (7) 격자 안에서 터지고 떨어지는 경우

## (8) 격자 안에서 단일 객체를 이동

## (9) 격자 안에서 여러 객제를 이동
<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3

```
</div>
</details>


# 2. 백트래킹
