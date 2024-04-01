# 💻삼성전자 코딩테스트 연습문제 오답정리
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
&emsp;[(1) K개 중 하나를 N번 선택하기](#1-K개-중-하나를-N번-선택하기)<br/>
&emsp;[(2) N개 중에 M개 고르기](#2-N개-중에-M개-고르기)<br/>

[3. 그래프 탐색](#3-그래프-탐색)<br/>
&emsp;[(1) DFS](#1-DFS)<br/>
&emsp;[(2) BFS 탐색](#2-BFS-탐색)<br/>
&emsp;[(3) 가중치가 동일한 그래프에서의 BFS](#3-가중치가-동일한-그래프에서의-BFS)<br/>
<br/>
<br/>


# 1. 시뮬레이션
## (1) dx dy technique

<details>
<summary>풀이 CODE</summary>
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

---

**오답 문제 1 : 행복한 수열의 개수**
+ 문제 상황
    + 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
    + n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램
    + ```1 ≤ m ≤ n ≤ 100```
+ 알고리즘 설계
    + 동일한 원소 개수 cnt = 1로 지정 / array 첫 번째 원소 = num으로 지정 후 다음 원소와 비교해가며 cnt & num 값 update
    + 원소 값이 동일하면 cnt를 더하고, 다르면 1로 초기화 / array 끝까지 도달했을 때 cnt가 m 이상일 경우 1을 반환
    + 각 열, 각 행마다 개수를 각각 도출해서 더하기로 결정
+ 틀린 이유
    + 함수 내에서 원소 값이 다르다고 cnt를 1로 초기화하면 안 됨
+ 수정
    + ```max_cnt = max(max_cnt, cnt)```을 통해 최대 cnt 값을 따로 저장해간 후 m 값과 비교하기
+ 느낀 점
    + 테스트케이스 이외의 다양한 반례 상황 찾아보기
<details>
<summary>풀이 CODE</summary>
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

---

**오답 문제 2 : 금 채굴하기**
+ 문제 상황
    + n × n 크기의 이차원 영역에 파묻힌 금 한 개의 가격이 m일 때, 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수를 출력
    + 채굴은 반드시 마름모 모양으로 단 한 번 가능
        + 마름모 모양 : 특정 중심점을 기준으로 K번 이내로 상하좌우의 인접한 곳으로 이동하는 걸 반복했을 때 갈 수 있는 모든 영역
    + 채굴에 드는 비용 = 마름모 안의 격자 개수 = ```K ∗ K + (K + 1) ∗ (K + 1)```로 계산
    + ```1 ≤ n ≤ 20 / 1 ≤ m ≤ 10```
+ 알고리즘 설계
    + 무한 loop 내에서 마름모의 중심을 n x n 격자 전체를 이중 for문으로 순회
    + 마름모 모양에 속하는 격자 내의 금의 개수를 cnt에 더하기
    + 마름모 중심마다 계산되는 값들의 최댓값을 max_cnt 값에 저장
    + K의 값은 손해가 나지 않는다면 result에 값을 담고, K + 1 / 아니면 break
+ 틀린 이유
    + if문에 의해 result 값이 설정되는 과정이 생략되는 반례가 존재했음
+ 수정
    + ```result = 0```을 통해 기본 result 값을 설정한 후 진행
+ 느낀 점
    + 방법론 생각하는 과정에서 시간 복잡도 계산하기
    + 변수 새로 설정 시 반례에 의한 기본값 설정의 필요성 확인하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def func1(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2)) <= k

k = 0
max_cnt = 0
result = 0
while True:
    for i in range(n):
        for j in range(n):
            cnt = 0
            for x in range(n):
                for y in range(n):
                    if func1(i, j, x, y):
                        cnt += array[x][y]
            max_cnt = max(cnt, max_cnt)
    cost = k ** 2  + (k + 1) ** 2
    if m * max_cnt >= cost:
        result = max_cnt
        k += 1
    else:
        break

print(result)
```
</div>
</details>

---

**오답 문제 3 : 겹쳐지지 않는 두 직사각형**
+ 문제 상황
    + n * m 크기의 이차원 영역의 각 위치에 정수 값이 하나씩 적혀있음
    + 영역 안에서 서로 겹치지 않는 두 직사각형을 적절하게 잡아, 두 직사각형 안에 적힌 숫자들의 총합을 최대로 하는 프로그램을 작성
    + 꼭 2개의 직사각형을 골라야만 하며, 두 직사각형의 경계는 서로 닿아도 됨
    + ```2 ≤ n, m ≤ 5 / -1,000 ≤ 정수 값 ≤ 1,000```
+ 알고리즘 설계
    + 좌측 상단과 우측 하단의 꼭짓점을 이중 for문을 통해 격자 내에서 설정해가며 직사각형 설정
    + 각 직사각형의 위치에 대해 0으로 이루어진 box array에 1을 더하고, 해당 정수들은 cnt 값에 더함
    + box array의 값이 1보다 크면 겹치는 직사각형이므로 result에 포함 X
+ 틀린 이유
    + 이중 for문 설계에 있어 연산 순서를 잘못 고려함
    + box을 box1과 box2로 나눠서 생각했어야 함
+ 수정
    + box1과 box2를 각각 계산한 후 (i, j) 순환하며 더하도록 if문 변경
+ 느낀 점
    + 다중 for 문을 사용할 때 연산 순서 유의
    + 함수화를 통한 코드 단순화의 필요

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

result = []
for x0 in range(n):
    for y0 in range(m):
        for x1 in range(x0, n):
            for y1 in range(y0, m):
                box1 = [[0] * m for _ in range(n)]
                cnt1 = 0
                for i1 in range(x0, x1 + 1):
                    for j1 in range(y0, y1 + 1):
                        cnt1 += array[i1][j1]
                        box1[i1][j1] += 1
                for x2 in range(n):
                    for y2 in range(m):
                        for x3 in range(x2, n):
                            for y3 in range(y2, m):
                                box2 = [[0] * m for _ in range(n)]
                                cnt2 = 0
                                for i2 in range(x2, x3 + 1):
                                    for j2 in range(y2, y3 + 1):
                                        cnt2 += array[i2][j2]
                                        box2[i2][j2] += 1

                                flag = True
                                for i in range(n):
                                    for j in range(m):
                                        if box1[i][j] + box2[i][j] > 1:
                                            flag = False
                                            
                                if flag:
                                    cnt = cnt1 + cnt2
                                    result.append(cnt)
print(max(result))
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

            
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

            
def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹치게 됩니다.
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False


# (x1, y1), (x2, y2) 그리고
# (x3, y3), (x4, y4) 로 이루어져있는
# 두 직사각형이 겹치는지 확인하는 함수
def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()


def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때
# 두 번째 직사각형을 겹치지 않게 잘 잡아
# 최대 합을 반환하는 함수
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    
    # (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 두 번째 직사각형을 정하여
    # 겹치지 않았을 때 중
    # 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, 
                                      rect_sum(x1, y1, x2, y2) +
                                      rect_sum(i, j, k, l))
    
    return max_sum


# 두 직사각형을 잘 잡았을 때의 최대 합을 반환하는 함수
def find_max_sum():
    max_sum = INT_MIN
    
	# (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 첫 번째 직사각형을 정하여
    # 그 중 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum,
                                  find_max_sum_with_rect(i, j, k, l))
    return max_sum


ans = find_max_sum()
print(ans)
```
</div>
</details>

---

## (6) 격자 안에서 밀고 당기기
**밀고 당기기**
+ 주어진 숫자들을 특정 방향으로 1칸씩 미는 작업
+ 선택된 행 : 왼쪽 혹은 오른쪽으로 한 칸씩 밀어주는 작업 / 선택된 열 : 위 혹은 아래 방향으로 한 칸씩 밀어주는 작업
+ temp 사용 : 가장 오른쪽에 있는 원소가 유실되서는 안됨
    + 가장 오른쪽에 있는 원소를 미리 temp라는 변수에 담기
    + temp 값을 미는 작업을 진행한 이후에 다시 첫 번째 원소에 넣어주기
+ 밀어주는 방향
    + 오른쪽으로 밀어주기 위해서는 가장 끝 칸부터 앞으로 오며 순서대로 채워주기
	```Python3
	temp = a[n-1]
	for i in range(n - 1, 0, -1):
	a[i] = a[i - 1]
	a[0] = temp
	```
	```Python3
	a.insert(0, a.pop()) # 오른쪽으로 밀기
	a.insert(len(a) - 1, a.pop(0)) # 왼쪽으로 밀기
	```
    + 위쪽으로 당기기 위해서는 위에서 아래로 내려오며 한 칸씩 당겨준 뒤, 다시 마지막 행에 temp 값을 넣어주기
	```Python3
	temp = a[0][col]
	for row in range(n - 1):
	a[row][col] = a[row + 1][col]
	a[n - 1][col] = temp
	```
---

**오답 문제 1 : 2차원 바람**
+ 문제 상황
    + N * M 행렬 모양의 건물에 총 Q번의 바람이 붐
    + 특정 직사각형 영역의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 shift 하고 해당 직사각형 내 영역에 있는 값들을 각각 자신의 위치를 기준으로 자신과 인접한 원소들과의 평균 값으로 바꿈
    + ```1 ≤ r1 < r2 ≤ N / 1 ≤ c1 < c2 ≤ M / 2 ≤ N ≤ 100 / 2 ≤ M ≤ 100 / 0 ≤ Q ≤ 100```
+ 알고리즘 설계
    + 직사각형 경계 row, column에 대하여 마지막에서 두 번째 값을 temp로 하나씩 저장 후 시계방향으로 하나씩 shift 진행
    + 인접 원소들의 평균값을 도출하는 함수 설정해 직사각형 영역을 순회하며 실행 후 new_array에 값을 저장
+ 틀린 이유
    + array 복사를 잘못하여 두 개가 동시에 값이 변경되는 문제가 발생
+ 수정
    + 아래와 같은 형식으로 deepcopy를 활용하여 2차원 배열 복사
      ```Python3
      from copy import deepcopy
      array = deepcopy(new_array)
      ```
+ 느낀 점
    + 해설처럼 하나만 temp를 설정한 후 순서대로 shift 한다면, temp를 여러 개 지정할 필요가 없음
    + 2차원 배열 array를 복사하는 데에 있어 deepcopy 방법을 암기할 것 

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
from copy import deepcopy
N, M, Q = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

def in_range(x, y):
    return (0 <= x and x < N) and (0 <= y and y < M)

def average_value(arr, x, y):
    sum_temp, cnt = 0, 0
    sum_temp += arr[x][y]
    cnt += 1
    if in_range(x - 1, y):
        sum_temp += arr[x - 1][y]
        cnt += 1
    if in_range(x, y + 1):
        sum_temp += arr[x][y + 1]
        cnt += 1
    if in_range(x + 1, y):
        sum_temp += arr[x + 1][y]
        cnt += 1
    if in_range(x, y - 1):
        sum_temp += arr[x][y - 1]
        cnt += 1
    return sum_temp // cnt

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    temp1 = array[r1 - 1][c2 - 2]
    temp2 = array[r2 - 2][c2 - 1]
    temp3 = array[r2 - 1][c1]
    temp4 = array[r1][c1 - 1]

    for i in range(c2 - 2, c1 - 1, -1):
        array[r1 - 1][i] = array[r1 - 1][i - 1]
    array[r1 - 1][c1 - 1] = temp4

    for i in range(r2 - 2, r1 - 1, -1):
        array[i][c2 - 1] = array[i - 1][c2 - 1]
    array[r1 - 1][c2 - 1] = temp1

    for i in range(c1, c2 - 1):
        array[r2 - 1][i] = array[r2 - 1][i + 1]
    array[r2 - 1][c2 - 1] = temp2

    for i in range(r1, r2 - 1):
        array[i][c1 - 1] = array[i + 1][c1 - 1]
    array[r2 - 1][c1 - 1] = temp3

    new_array = deepcopy(array)
    for x in range(r1 - 1, r2):
        for y in range(c1 - 1, c2):
            new_array[x][y] = average_value(array, x, y)
    array = deepcopy(new_array)

for i in array:
    print(*i)
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력
n, m, q = tuple(map(int, input().split()))
a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]
temp_arr = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


# 직사각형의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전해줍니다.
def rotate(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
    temp = a[start_row][start_col]
    
    # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        a[row][start_col] = a[row + 1][start_col]
    
    # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        a[end_row][col] = a[end_row][col + 1]
    
    # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        a[row][end_col] = a[row - 1][end_col]
    
    # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        a[start_row][col] = a[start_row][col - 1]
    
    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 넣습니다.
    a[start_row][start_col + 1] = temp


# 격자를 벗어나는지 판단합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m


# x행 y열 (x, y)과 인접한 숫자들과의 평균 값을 계산해줍니다.
# 격자를 벗어나지 않는 숫자들만을 고려해줍니다.
def average(x, y):
    # 자기 자신의 위치를 포함하여 평균을 내야 하므로
    # dx, dy 방향을 5개로 설정하면 한 번에 처리가 가능합니다.
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    
    active_numbers = [
        a[x + dx][y + dy]
        for dx, dy in zip(dxs, dys)
        if in_range(x + dx, y + dy)
    ]
    
    return sum(active_numbers) // len(active_numbers)


# 직사각형 내 숫자들을 인접한 숫자들과의 평균값으로 바꿔줍니다.
# 동시에 일어나야 하는 작업이므로, 이미 바뀐 숫자에 주위 숫자들이 영향을 받으면 안되기 때문에
# temp_arr 배열에 평균 값들을 전부 적어 준 다음, 그 값을 다시 복사해 옵니다.
def set_average(start_row, start_col, end_row, end_col):
    # Step2-1. temp_arr에 평균 값을 적습니다.
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = average(row, col)
    
    # Step2-2. temp_arr 값을 다시 가져옵니다.
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            a[row][col] = temp_arr[row][col]


# 조건에 맞춰 값을 바꿔봅니다.
def simulate(start_row, start_col, end_row, end_col):
    # Step1
    # 직사각형 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전해줍니다.
    rotate(start_row, start_col, end_row, end_col)
    
    # Step2
    # 직사각형 내 각각의 숫자들을 인접한 숫자들과의 평균값으로 바꿔줍니다.
    set_average(start_row, start_col, end_row, end_col)


for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    
    # 조건에 맞춰 값을 바꿔봅니다.
    simulate(r1, c1, r2, c2)

# 출력
for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end = " ")
    print()
```
</div>
</details>

---

**오답 문제 2 : 최단 Run Length 인코딩**
+ 문제 상황
    + 길이가 n인 문자열 A가 주어졌을 때, 적절하게 특정 횟수만큼 오른쪽으로 shift하여, shift 된 이후의 문자열에 Run-Length Encoding을 진행했을 때의 최소 길이를 구하기
    + Run-Length Encoding : 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식
    	+ aaabbbbcaa $\rightarrow$  a3b4c1a2
    + ```1 ≤ 문자열 A의 길이 ≤ 10```
+ 알고리즘 설계
    + 반복문을 통해 최소 1부터 최대 문자열의 길이만큼 오른쪽 shift하며 Encoding 결과 길이 계산
    + 함수화를 통해 Encoding 하는 과정 설정 : 기준값(std)과 개수(cnt) 활용해서 문자열을 순회하며 동작
+ 틀린 이유
    + 문자열의 길이가 1인 경우를 고려하지 않음
+ 수정
    + 함수에 문자열의 길이가 1인 경우를 if문을 통해 따로 구별
+ 느낀 점
    + 함수 설정에 있어 모든 경우의 수를 포함하는지 확인하기
    + 함수를 단순화할 수 있는 방법 생각하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
A = list(input())
n = len(A)
result = []

def func(array):
    std = array[0]
    cnt = 1
    word_label = ''
    if len(array) == 1:
        word = str(std) + str(cnt)
        word_label = word_label + word
    for i in range(len(array) - 1):
        if array[i + 1] == std:
            cnt += 1
            if (i + 1) == len(array) - 1:
                word = str(std) + str(cnt)
                word_label = word_label + word
        else:
            word = str(std) + str(cnt)
            word_label = word_label + word
            std = array[i + 1]
            cnt = 1
            if (i + 1) == len(array) - 1:
                word = str(std) + str(cnt)
                word_label = word_label + word
    return word_label

for i in range(1, n + 1):
    array = A[:]
    for _ in range(i):
        array.insert(0, array.pop())
    result.append(len(func(array)))

print(min(result))
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력:
A = input()


def run_length_encoding(target):
    # 이 함수는 input 문자열을 Run-Length-Encoding한 결과를 반환합니다.
    encoded = ""

    # 입력의 첫번째 값을 읽고 초기화합니다.
    curr_char = target[0]
    num_char = 1
    for target_char in target[1:]:
        if target_char == curr_char:
            num_char += 1
        else:
            # 지금까지 세어온 curr_char와 num_char를 기록합니다.
            encoded += curr_char
            encoded += str(num_char)
    
            # curr_char와 num_char를 현재 값으로 초기화합니다.
            curr_char = target_char
            num_char = 1
        
    # 마지막 덩어리에 해당하는 curr_char와 num_char를 기록합니다.
    encoded += curr_char
    encoded += str(num_char)
    return encoded


min_length = len(run_length_encoding(A)) # 초기값은 shift안했을 때의 값
n = len(A)
num_shift = n - 1 # 0부터 length - 1

while num_shift:
    # 문자열 A를 오른쪽으로 1번 shift합니다.
    A = A[-1] + A[:-1]
    
    length = len(run_length_encoding(A))
    if min_length > length:
        min_length = length
    
    num_shift -= 1
    
# 출력
print(min_length)
```
</div>
</details>

---

## (7) 격자 안에서 터지고 떨어지는 경우
**격자 안에서 터지고 떨어지는 작업**
+ 특정 규칙에 의해 폭탄이 터지게 되고, 그 이후에 중력이 작용하여 위에 떠있는 폭탄들이 아래로 떨어지는 작업
+ 새로운 temp 배열을 이용하는 방법 : 시간복잡도 O(n)
+ 2차원 격자에서 폭탄들이 떨어질 때 : 폭탄들이 떨어지는 과정은 각 열에 대해 독립적으로 진행
    1. temp 배열을 새로 만들어줌
    2. 아래에서 위로 올라오면서, 비어있지 않을 때만 temp에 넣어줌
		+ temp의 해당 col열의 가장 밑에서부터 폭탄을 채워줌
  		+ 단, arr의 col열의 가장 밑에서부터 올라오며 폭탄이 있는 경우에만 temp에 옮겨줌
  		+ row값을 n - 1에서부터 0으로 감소시키며 하나씩 조사하며, temp를 위한 temp_row값을 정의하여 n - 1에서부터 순서대로 1씩 감소하며 채움
    3. temp 값을 기존 배열에 다시 옮겨줌
	```Python3
	BLANK = 0
	n = 6
	arr = [[0] * n for _ in range(n)]
	temp = [[0] * n for _ in range(n)]
	
	for row in range(n - 1, -1, -1):
	    temp[row][col] = BLANK
	
	temp_row = n - 1
	
	for row in range(n - 1, -1, -1):
	    if arr[row][col] != BLANK:
	        temp[temp_row][col] = arr[row][col]
	        temp_row -= 1
	
	for row in range(n):
	    arr[row][col] = temp[row][col]
	```
	```Python3
	# filter를 사용하는 방법도 존재
	temp = list(filter(lambda x: x > 0, array[row]))
	array[row] = temp + [0] * (n - len(temp))
	```
 
+ 1차원 격자에서 폭탄들이 떨어질 때 : 1차원 배열 내에서 특정 구간의 원소가 삭제된 것과 같이, 뒤에 남은 원소들을 앞으로 당겨주는 시뮬레이션을 진행
    1. temp라는 이름의 1차원 배열을 새로 만들어줌 / end_of_temp_array라는 변수도 선언해주며 초기값으로 0을 넣어줍
    2. 왼쪽에서 오른쪽으로 가면서, 비어있지 않을 때만 temp에 넣어줌
		+ temp의 왼쪽에서부터 폭탄을 채워줌
  		+ 단, arr의 해당 index에 폭탄이 있는 경우에만 temp에 옮겨줌
  		+ index값을 0에서 end_of_array까지 1씩 증가시키며 하나씩 조사하며, temp를 위한 end_of_temp_array값을 0에서부터 순서대로 1씩 증가시키며 채움
    3. temp 값을 기존 배열에 다시 옮겨줌
	```Python3
	BLANK = 0
	end_of_array = 6
	arr = [0] * 6
	temp = [0] * 6
	
	end_of_temp_array = 0
	
	for i in range(end_of_array):
	    if arr[i] != BLANK:
	        temp[end_of_temp_array] = arr[i]
	        end_of_temp_array += 1
	
	for i in range(end_of_temp_array):
	    arr[i] = temp[i]
	
	end_of_array = end_of_temp_array
	```
---

**오답 문제 1 : 2차원 폭발 게임**
+ 문제 상황
    + 1이상 100이하의 숫자가 적혀있는 폭탄이 N × N 크기의 상자에 들어있음
    + 각각의 열에 대하여 행 기준으로 봤을 때 연속으로 M개 이상의 같은 숫자가 적혀있는 폭탄들은 터지게 되고, 중력에 의해 위에 있던 폭탄들은 밑으로 떨어짐
    	+ M개 이상인 폭탄들의 쌍이 여러 개라면 동시에 터짐
    	+ 터져야 할 폭탄이 없을 때까지 조건에 맞는 폭탄들을 터뜨리는 것을 반복
    + 터지는 과정을 한번 반복한 이후에는 상자를 시계방향으로 90° 회전
    	+ 회전 이후 중력에 의해 밑에 여유 공간이 있을 경우 밑으로 떨어짐
    + 폭탄들이 움직이지 않게 되면 다시 각각의 열마다 행을 기준으로 연속으로 M개 이상의 같은 숫자가 적혀있는 폭탄들은 터지게 되고 다시 중력에 의해 밑으로 떨어짐
    + 이와 같이 터지고 회전하는 과정을 총 K번 반복한다고 했을 때, 최종적으로 상자에 남아있는 폭탄의 수를 출력하는 프로그램을 작성
    + 만약 K번째 회전을 진행한 이후에도 터질 폭탄이 상자에 남아있다면, 조건에 맞는 폭탄들을 전부 터뜨리는 것을 반복한 이후에 최종적으로 상자에 남아 있는 폭탄의 수를 구하기
    + ```1 ≤ N ≤ 100 / 1 ≤ M ≤ 100 / 1 ≤ K ≤ 1,000```
+ 알고리즘 설계
    + explosion_end_idx 함수를 통해 특정 연속 값의 마지막 index 반환
    + bomb 함수를 통해 연속 M개 이상의 같은 숫자가 있을 경우 폭탄들이 터지고, 중력으로 떨어지는 과정을 가능할 때까지 무한 반복
    + rotate 함수를 통해 90도 회전하고 중력에 의해 떨어지게 설정
+ 틀린 이유
    + rotate 함수 내에서 90도 회전만 하고, 중력에 의해 떨어지는 것을 고려하지 못함
+ 수정
    + rotate 함수 내에 중력 영향 구현
+ 느낀 점
    + 연속 값의 개수를 세는 방법론 기억해두기
    + 문제 조건 꼼꼼히 확인하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
blank = 0
N, M, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

def explosion_end_idx(array, start_idx, value):
    for end_idx in range(start_idx + 1, N):
        if array[end_idx] != value:
            return end_idx - 1
    return N - 1

def bomb(array):
    while True:
        flag = False
        for col in range(N):
            temp = []
            for row in range(N):
                temp.append(array[row][col])
            for idx, value in enumerate(temp):
                if value == blank:
                    continue
                end_idx = explosion_end_idx(temp, idx, value)
                if end_idx - idx + 1 >= M:
                    temp[idx : end_idx + 1] = [0] * (end_idx - idx + 1)
                    flag = True
            temp = list(filter(lambda x : x > 0, temp))
            temp = [0] * (N - len(temp)) + temp
            for row in range(N):
                array[row][col] = temp[row]
        if not flag:
            break
    return array

def rotate(array):
    temp = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            temp[col][N - 1 - row] = array[row][col]
    for col in range(N):
        gravity_temp = []
        for row in range(N):
            gravity_temp.append(temp[row][col])
        gravity_temp = list(filter(lambda x : x > 0, gravity_temp))
        gravity_temp = [0] * (N - len(gravity_temp)) + gravity_temp
        for row in range(N):
            temp[row][col] = gravity_temp[row]
    return temp

for _ in range(K):
    array = bomb(array)
    array = rotate(array)

array = bomb(array)

cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] > 0:
            cnt += 1
print(cnt)
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
BLANK = -1
WILL_EXPLODE = 0

# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
numbers_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]
numbers_1d = [
    0 for _ in range(n)
]


# 주어진 시작점에 대하여
# 부분 수열의 끝 위치를 반환합니다.
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers_1d)):
        if numbers_1d[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers_1d) - 1


def explode():
    while True:
        did_explode = False
        curr_idx = 0
    
        while curr_idx < len(numbers_1d):
            end_idx = get_end_idx_of_explosion(curr_idx, numbers_1d[curr_idx])
        
            if end_idx - curr_idx + 1 >= m:
                # 연속한 숫자의 개수가 m개 이상이면
                # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
                # 폭탄이 터졌음을 기록해줍니다.
                del numbers_1d[curr_idx:end_idx + 1]
                did_explode = True
            else:
                # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
                # 다음 원소에 대하여 탐색하여 줍니다.
                curr_idx = end_idx + 1

        if not did_explode:
            break


##################################################################################
##			이 줄을 기준으로 위에 있는 함수들에 대한 설명은 1차원 폭발 게임을 참조해주세요     	  ##
##################################################################################

        
# 격자의 특정 열을 일차원 배열에 복사해줍니다.
def copy_column(col):
    global numbers_1d
    
    numbers_1d = [
        numbers_2d[row][col]
        for row in range(n)
        if numbers_2d[row][col] != BLANK
    ]


# 폭탄이 터진 결과를 격자의 해당 열에 복사해줍니다.
def copy_result(col):
    for row in range(n - 1, -1, -1):
        numbers_2d[row][col] = numbers_1d.pop() if numbers_1d \
                                                else BLANK


# 폭탄이 터지는 과정을 시뮬레이션 합니다.
def simulate():
    for col in range(n):
        copy_column(col)
        explode()
        copy_result(col)

        
# 시계 방향으로 90도 회전해줍니다.
def rotate():
    global numbers_2d
    
    # 빈 칸으로 초기화 된 임시 격자를 선언합니다.
    temp_2d = [
        [BLANK for _ in range(n)]
        for _ in range(n)
    ]
    
    # 기존 격자를 시계 방향으로 90도 회전했을 때의 결과를
    # 임시 격자에 저장해줍니다.
    for i in range(n - 1, -1, -1):
        curr_idx = n - 1
        for j in range(n - 1, -1, -1):
            if numbers_2d[i][j] != BLANK:
                temp_2d[curr_idx][n - i - 1] = numbers_2d[i][j]
                curr_idx -= 1
    
    # 임시 격자에 저장된 값을 기존 격자에 복사합니다.
    numbers_2d = temp_2d

        
# 주어진 입력에 따라 폭탄이 터지는 것을 시뮬레이션 합니다.
simulate()
for _ in range(k):
    rotate()
    simulate()

        
# 격자를 순회하며 남아 있는 폭탄의 개수를 세줍니다.
answer = sum([
    numbers_2d[i][j] != BLANK
    for i in range(n)
    for j in range(n)
])
print(answer)
```
</div>
</details>

---

## (8) 격자 안에서 단일 객체를 이동
**2차원 격자 안에서 단일 객체를 이동하는 시뮬레이션**
+ dx, dy 테크닉을 문제 정의에 맞게 이용하는 것이 중요
```Python3
def simulate():
    global curr_x, curr_y
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num = 0
    max_pos = (-1, -1)
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
    curr_x, curr_x = max_pos
```

---

**오답 문제 1 : 숫자가 더 큰 인접한 곳으로 이동**
+ 문제 상황
    + 1이상 100이하의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어짐
    + 특정 위치에서 시작하여, 상하좌우로 인접한 곳에 있는 숫자들 중 현재 위치에 있는 숫자보다 더 큰 위치로 끊임없이 이동
    + 그러한 위치가 여러개 있는 경우, 상하좌우 방향 순서대로 우선순위를 매겨 가능한 곳 중 우선순위가 더 높은 곳으로 이동
    + 격자를 벗어나서는 안되며, 더 이상 움직일 수 없을 때까지 반복
    + ```1 ≤ r, c ≤ n / 1 ≤ n ≤ 100```
+ 알고리즘 설계
    + 입력받은 위치를 global 변수 x, y에 할당하고 simulate() 함수를 통해 이동한 위치가 기존 최댓값보다 클 경우 max_pos, max_value를 update
    + while True를 통해 max_value를 result라는 list에 계속 담게 설정하며 만약 새로 담을 값이 result[-1] 값과 동일할 경우 break
+ 틀린 이유
    + global 변수를 설정하는데에 어려움이 있었고, 반복문을 탈출하지 못함
+ 수정
    + max_pos, max_value에 대해서도 global 변수 설정
    + 결과값을 담은 list와 비교해 무한 반복문 탈출
+ 느낀 점
    + simulate() 함수 자체에서 True, False 값을 return 하는 방법이 더 효율적. 결과값을 통해 무한반복문에서 탈출하기 용이함
    + global 변수 설정의 필요성에 대해 알아두기
    + 입력이 없는 함수에 대해 익숙해지기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n, r, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

result = []
x, y = r - 1, c - 1
max_pos = (r - 1, c - 1)
max_value = array[r - 1][c - 1]

def simulate():
    global x, y, max_pos, max_value 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and array[nx][ny] > max_value:
            max_pos = (nx, ny)
            max_value = array[nx][ny]
            break
    x, y = max_pos
    return max_value

while True:
    result.append(max_value)   
    if simulate() == result[-1]:
        print(*result)
        break
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력
n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문하게 되는 숫자들을 담을 곳입니다.
visited_nums = []


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인합니다.
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num


# 조건에 맞춰 움직여봅니다.
# 움직였다면 true를 반환하고
# 만약 움직일 수 있는 곳이 없었다면 false를 반환합니다.
def simulate():
    global curr_x, curr_y
    
    # 코딩의 간결함을 위해 
    # 문제 조건에 맞게 상하좌우 순서로
    # 방향을 정의합니다.
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        # 갈 수 있는 곳이라면
        # 이동하고 true를 반환합니다.
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True
    
    # 움직일 수 있는 곳이 없었다는 의미로
    # false 값을 반환합니다.
    return False


# 초기 위치에 적혀있는 값을 답에 넣어줍니다.
visited_nums.append(a[curr_x][curr_y])
while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = simulate()
    
    # 인접한 곳에 더 큰 숫자가 없다면 종료합니다.
    if not greater_number_exist:
        break
    
    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited_nums.append(a[curr_x][curr_y])

# 출력:
for num in visited_nums:
    print(num, end=' ')
```
</div>
</details>

---

## (9) 격자 안에서 여러 객제를 이동
**오답 문제 1 : 000**
+ 문제 상황
    + 
+ 알고리즘 설계
    + 
+ 틀린 이유
    + 
+ 수정
    + 
+ 느낀 점
    + 

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3

```
</div>
</details>

---

# 2. 백트래킹
## (1) K개 중 하나를 N번 선택하기

## (2) N개 중에 M개 고르기

# 3. 그래프 탐색
## (1) DFS

## (2) BFS 탐색

## (3) 가중치가 동일한 그래프에서의 BFS
