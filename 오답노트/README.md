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
    	+ aaabbbbcaa $\rightarrow$ a3b4c1a2
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

**오답 문제 2 : 벽 짚고 미로 탈출하기**
+ 문제 상황
    + N * N 크기의 격자 안에서 주어진 위치에서 우측 방향을 바라보고 시작하여 오른쪽 벽을 짚고 쭉 따라가는 방식으로 미로를 탈출하는 프로그램을 작성
    + 규칙에 맞게 이동하다 격자 밖을 벗어났을 때 미로를 탈출 한 것으로 가정
    + 벽을 짚고 탈출하는 방식
     	+ 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우 : 반 시계 방향으로 90' 만큼 회전
      	+ 바라보고 있는 방향으로 이동하는 것이 가능한 경우 : 바로 앞이 격자 밖이라면 이동하여 탈출
      		+ 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면 그 방향으로 한 칸 이동
       		+ 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않는다면, 현재 방향으로 한 칸 이동 후 방향을 시계 방향으로 90' 만큼 방향을 틀어 한 칸 더 전진하여 오른쪽에 벽이 있게함
    + 방향을 트는 데에는 시간이 걸리지 않고 한 번 이동하는 데에는 1초의 시간이 걸린다고 했을 때, 미로를 탈출하는 데 걸리는 시간을 출력
    + 오른쪽 벽을 짚고 따라가는 방식만으로 미로를 탈출하는 것이 불가능하다면 -1을 출력
    + ```2 ≤ N ≤ 100```
+ 알고리즘 설계
    + 이동하게 될 위치를 next_x, next_y라 하고 해당 값이 격자를 벗어날 경우 탈출이라 판정하고 time을 담은 result 값 및 False return하기
    + 탈출하지 못할 경우 규칙에 맞게 이동
    + 미로 속에 갇혀 있는 경우 result 값에 time을 부여하지 않고 바로 False return하기
+ 틀린 이유
    + 미로 속에 갇혀 있는 경우를 고려하지 못함
    + visited을 통해 해결하려 했지만 방향까지 일치해야 완전히 갇혀있다는 것을 파악하지 못함
+ 수정
    + time이 0보다 크고, dir_change가 0보다 크다면 이동 또는 방향 회전을 한 것이므로 해당 경우에 대해 위치와 방향이 일치한지 확인
+ 느낀 점
    + 다양한 테스트 케이스를 고려하여 문제를 해결할 것
    + 해설 CODE 처럼 visited을 삼중 리스트로 만들어 방향 일치여부까지 한 번에 확인하는 것이 더 효율적인 방법

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n = int(input())
x, y = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(input()))

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

curr_x, curr_y = x - 1, y - 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num, dir_change, time, result = 0, 0, 0, -1

def simulate():
    global curr_x, curr_y, dir_num, dir_change, time, result
    next_x = curr_x + dx[dir_num]
    next_y = curr_y + dy[dir_num]
    if not in_range(next_x, next_y):
        time += 1
        result = time
        return False
    else:
        if time > 0 or dir_change > 0:
            if (curr_x, curr_y) == (x - 1, y - 1) and dir_num == 0:
                return False
        if array[next_x][next_y] == '#':
            dir_num = (dir_num + 3) % 4
            dir_change += 1
        else:
            wall_dir = (dir_num + 1) % 4
            wall_x = next_x + dx[wall_dir]
            wall_y = next_y + dy[wall_dir]
            if array[wall_x][wall_y] == '#':
                time += 1
                curr_x, curr_y = next_x, next_y
            else:
                time += 1
                curr_x, curr_y = next_x, next_y
                dir_num = wall_dir        
    return True

while True:
    if not simulate():
        print(result)
        break
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
import sys

DIR_NUM = 4

# 변수 선언 및 입력
n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 미로 탈출이 불가능한지 여부를 판단하기 위해
# 동일한 위치에 동일한 방향으로 진행했던 적이 있는지를
# 표시해주는 배열입니다.
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
elapsed_time = 0

# 처음에는 우측 방향을 바라보고 시작합니다.
curr_dir = 0


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 위치에 벽이 있으면 이동이 불가합니다.
def wall_exist(x, y):
    return in_range(x, y) and a[x][y] == '#'


# 조건에 맞춰 움직여봅니다.
def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time
    
    # 현재 위치에 같은 방향으로 진행한 적이 이미 있었는지 확인합니다.
    # 이미 한 번 겪었던 상황이라면, 탈출이 불가능 하다는 의미이므로 
    # -1을 출력하고 프로그램을 종료합니다.
    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0)
    
    # 현재 상황이 다시 반복되는지를 나중에 확인하기 위해
    # 현재 상황에 해당하는 곳에 visited 값을 True로 설정합니다.
    visited[curr_x][curr_y][curr_dir] = True
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    
    # Step1
    
    # 바라보고 있는 방향으로 이동하는 것이 불가능한 경우에는
    # 반 시계 방향으로 90' 방향을 바꿉니다.
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir - 1 + 4) % 4
    
    # Step2
    
    # Case1
    # 바라보고 있는 방향으로 이동하는 것이 가능한 경우 중
    # 바로 앞이 격자 밖이라면 탈출합니다.
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1
    
    # Case 2 & Case 3
    # 바로 앞이 격자 안에서 이동할 수 있는 곳이라면
    else:
        # 그 방향으로 이동했다 가정헀을 때 바로 오른쪽에 짚을 벽이 있는지 봅니다.
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]
        
        # Case2
        # 그대로 이동해도 바로 오른쪽에 짚을 벽이 있다면
        # 해당 방향으로 한 칸 이동합니다.
        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1
        
        # Case3
        # 그렇지 않다면 2칸 이동후 방향을 시계방향으로 90' 방향을 바꿉니다.
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2


for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(curr_x, curr_y):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(elapsed_time)
```
</div>
</details>

---

**오답 문제 3 : 뱀은 사과를 좋아해**
+ 문제 상황
    + N * N 크기의 격자 안에서 사과들의 위치와 뱀의 움직임이 주어졌을 때, 게임이 끝나는데 몇 초가 걸리는지를 구하기
    + 뱀은 처음에 좌측 상단 (1, 1)에서 길이 1의 상태로 존재
    + 뱀은 이동시에 머리를 특정 방향으로 한 칸 옮기게 되고, 가장 끝에 있던 꼬리가 사라지게 되며 이 과정은 동시에 일어남
    + 만약 움직인 장소에 사과가 존재한다면 꼬리가 사라지지 않고 몸의 길이가 1 늘어나게 됩니다. 또, 사과는 먹는 즉시 사라짐
    + 뱀이 움직이는 데에는 1초의 시간이 소요
    + 게임은 뱀이 전부 움직였거나, 움직이는 도중 격자를 벗어났거나, 움직이는 도중 몸이 꼬여 서로 겹쳐졌을 경우 종료
    + ```1 ≤ p ≤ 100 / 1 ≤ N ≤ 100 / 0 ≤ M < N * N / 0 ≤ K ≤ 1,000 / 0 ≤ 입력으로 주어지는 전체 p의 합 (S) ≤ 10,000```
+ 알고리즘 설계
    + 뱀의 위치를 머리 - 꼬리 순으로 visited에 저장
    + simulate() 함수를 설정
    	+ 사과를 먹었을 때 ```length += 1```, 이동 시 ```time += 1``` 격자를 벗어날 경우 False를 return
        + 뱀의 이동 후 위치를 담은 new_visited에 대해 새로운 머리 위치 + 기존 위치에서 (길이 - 머리 크기 1)만큼 몸통 가져오기
+ 틀린 이유
    + 시간 초과 발생
+ 수정
    + 불가
+ 느낀 점
    + 자료형 사용에 있어 시간 복잡도 고려하기
    + 해설 코드와 같은 함수화 작업하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n, m, k = map(int, input().split())
array = []
visited = [[0, 0]]
dir_list = []
dir_dict = {'R' : 0,
            'D' : 1,
            'L' : 2,
            'U' : 3}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(m):
    x, y = map(int, input().split())
    array.append([x - 1, y - 1])

for _ in range(k):
    d, p = input().split()
    p = int(p)
    for _ in range(p):
        dir_list.append(dir_dict[d])

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

time = 0
length = 1
limit_time = len(dir_list)

def simulate():
    global array, visited, time, length
    curr_x, curr_y = visited[0][0], visited[0][1]
    if time == limit_time:
        return False
    dir_idx = dir_list[time]
    next_x = curr_x + dx[dir_idx]
    next_y = curr_y + dy[dir_idx]
    time += 1
    if not in_range(next_x, next_y):
        return False    
    # 새로운 head 위치에 사과 존재
    if [next_x, next_y] in array:
        length += 1
        array.remove([next_x, next_y])
    
    new_visited = [[next_x, next_y]] + visited[:length - 1]
    if [next_x, next_y] in visited[:length - 1]:
        return False
    visited = [v[:] for v in new_visited]
    return True

while True:
    if not simulate():
        print(time)
        break
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력
n, m, K = tuple(map(int, input().split()))
apple = [
    [False for _ in range(n + 1)]
    for _ in range(n + 1)
]
# 뱀은 처음에 (1, 1)에서 길이 1의 상태로 있습니다.
snake = [(1, 1)]

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}

ans = 0


# (x, y)가 범위 안에 들어가는지 확인합니다.
def can_go(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 뱀이 꼬였는지 확인합니다.
def is_twisted(new_head):
    return new_head in snake


# 새로운 머리를 추가합니다.
def push_front(new_head):
    # 몸이 꼬이는 경우
    # false를 반환합니다.
    if is_twisted(new_head):
        return False
    
    # 새로운 머리를 추가합니다.
    snake.insert(0, new_head)
    
    # 정상적으로 머리를 추가했다는 의미로
    # True를 반환합니다.
    return True


# 꼬리를 지웁니다.
def pop_back():
    snake.pop()


# (nx, ny)쪽으로 뱀을 움직입니다.
def move_snake(nx, ny):
    # 머리가 이동할 자리에 사과가 존재하면
    # 사과는 사라지게 되고
    if apple[nx][ny]:
        apple[nx][ny] = False
        # 꼬리는 사라지지 않고 머리만 늘어납니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    else:
        # 사과가 없으면 꼬리는 사라지게 되고
        pop_back()
        
        # 머리는 늘어나게 됩니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    
    # 정상적으로 뱀이 움직였으므로
    # True를 반환합니다.
    return True


# 뱀을 move_dir 방향으로 num번 움직입니다.
def move(move_dir, num):
    global ans
    
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # num 횟수만큼 뱀을 움직입니다.
    # 한 번 움직일때마다 답을 갱신합니다.
    for _ in range(num):
        ans += 1
        
        # 뱀의 머리가 그다음으로 움직일
        # 위치를 구합니다.
        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]
        
        # 그 다음 위치로 갈 수 없다면
        # 게임을 종료합니다.
        if not can_go(nx, ny):
            return False
        
        # 뱀을 한 칸 움직입니다.
        # 만약 몸이 꼬인다면 False를 반환합니다.
        if not move_snake(nx, ny):
            return False
    
    # 정상적으로 명령을 수행했다는 의미인 True를 반환합니다.
    return True


# 사과가 있는 위치를 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    apple[x][y] = True

# K개의 명령을 수행합니다.
for _ in range(K):
    # move_dir 방향으로 num 횟수 만큼 움직여야 합니다.
    move_dir, num = tuple(input().split())
    num = int(num)
    
    # 움직이는 도중 게임이 종료되었을 경우
    # 더 이상 진행하지 않습니다.
    if not move(mapper[move_dir], num):
        break

print(ans)
```
</div>
</details>

---

## (9) 격자 안에서 여러 객제를 이동
**2차원 격자 위에서 여러 객체를 이동**
+ dx, dy 테크닉을 이용
+ 각 객체가 어느 위치에 있는지를 잘 관리하는 것이 중요
+ 1차원 리스트를 만들어 각 객체의 위치를 관리하는 식으로 진행할 수도 있지만, 일반적으로는 2차원 격자 상에서 각 칸 단위로 객체를 관리하는 것이 더 좋음
+ 동시에 변화가 일어나야 하는 경우에는 새로운 배열을 만들어 주는 것이 항상 좋음

**오답 문제 1 : 벽이 있는 충돌 실험**
+ 문제 상황
    + M개의 구슬이 N*N 격자 안에 놓여져 있고, 격자는 벽으로 둘러싸여 있음
    + 구슬이 벽에 부딪히면 움직이지 않고 움직이는 방향만 반대로 뒤집힘 : 방향을 바꾸는 작업에는 1초의 시간이 소요
    + 두 개 이상의 구슬이 충돌하게 되면 부딪힌 구슬 모두 사라지게 됨
    + 충돌은 두 구슬이 이동 후 같은 위치에 있는 경우에만 일어남
    + 이동 중에 만나는 경우라면, 서로 충돌이 일어나지 않음
    + 각 구슬의 초기상태가 주어졌을 때, 아주 오랜시간이 흐른 후에도 여전히 격자 안에 남아있는 구슬의 개수를 출력하는 프로그램을 작성
    + ```1 ≤ T ≤ 100 / 1 ≤ N ≤ 50 / 0 ≤ M ≤ N * N```
+ 알고리즘 설계
    + 각 array는 구슬의 방향 dir_idx(0 ~ 3)을 담고 있으며 구슬이 없는 곳은 -1의 값을 가짐
    + in_range 함수를 통해 격자 내에 위치하는지 확인
    + move 함수를 통해 특정 구슬 움직이기
    	+ 이동 후 구슬 위치 (nx, ny)가 격자 내에 있다면 ```next_array[nx][ny] = dir_idx```. 이후 ```count[nx][ny] += 1, count[x][y] -= 1```
 	+ 격자 내에 없다면 방향만 전환
    + move_all 함수를 통해 모든 구슬 움직이기
        + next_array의 모든 값 -1로 초기화
        + array 값이 -1보다 크면, 즉 구슬이 있다면 move 함수 호출
    + delete 함수를 통해 충돌 구슬들 제거
      	+ count 값이 1보다 크면 충돌이므로, 0으로 변환하고 next_array의 해당 위치를 -1, 즉 구슬 없는 것으로 변환
      	+ next_array의 값을 array 값에 대입
    + simulate 함수를 통해 move_all 함수와 delete 함수 호출
    + 왕복 이동에 걸리는 2 * N 시간 만큼 simulate 반복
+ 틀린 이유
    + 동시 변화 발생으로 count에 대한 next_count을 생성했지만, 서로 구슬이 교차될 때 문제가 발생함
+ 수정
    + array에 대한 next_array를 생성해 구슬이 교차될 때도 이후의 방향 값에 대한 정보를 저장할 수 있음
+ 느낀 점
    + 동시에 변화가 발생할 때 어떤 것에 대해 새로운 배열을 추가로 생성해야 하는지, 언제 초기화 작업을 수행해야 하는지 확인하기
    + 시간 복잡도를 고려하고, 초기 상태로 돌아가기 위한 최소 반복 횟수에 대해 확인하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    array = [[-1] * N for _ in range(N)]
    next_array = [[-1] * N for _ in range(N)]
    count = [[0] * N for _ in range(N)]
    direction = {'D':0,
                'L':1,
                'R':2,
                'U':3}
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x), int(y)
        dir_idx = direction[d]
        array[x - 1][y - 1] = dir_idx
        next_array[x - 1][y - 1] = dir_idx
        count[x - 1][y - 1] += 1
    
    def in_range(x, y):
        return (0 <= x and x < N) and (0 <= y and y < N)

    def move(x, y, dir_idx):
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]
        if in_range(nx, ny):
            next_array[nx][ny] = dir_idx
            count[nx][ny] += 1
            count[x][y] -= 1
        else:
            next_array[x][y] = 3 - dir_idx
        
    def move_all():
        for i in range(N):
            for j in range(N):
                next_array[i][j] = -1
        for i in range(N):
            for j in range(N):
                if array[i][j] > -1:
                    x, y, dir_idx = i, j, array[i][j]
                    move(x, y, dir_idx)
    def delete():
        for i in range(N):
            for j in range(N):
                if count[i][j] > 1:
                    count[i][j] = 0
                    next_array[i][j] = -1
        for i in range(N):
            for j in range(N):
                array[i][j] = next_array[i][j]
    def simulate():
        move_all()
        delete()

    for _ in range(2 * N):
        simulate()

    cnt = 0
    for row in count:
        cnt += sum(row)
    
    print(cnt)
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
MAX_N = 50

# 변수 선언 및 입력
t = int(input())
n, m = 0, 0
marbles = []
marble_cnt = [
    [0 for _ in range(MAX_N + 1)]
    for _ in range(MAX_N + 1)
]

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}


# 해당 위치가 격자 안에 들어와 있는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 구슬이 1초 후에 어떤 위치에서 어떤 방향을 보고 있는지를 구해
# 그 상태를 반환합니다.
def move(marble):
    # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
    # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    x, y, move_dir = marble
    
    # 바로 앞에 벽이 있는지를 판단합니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
    if in_range(nx, ny):
        return (nx, ny, move_dir)
    # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
    # 위에서 dx, dy를 move_dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록
    # 설정해놨기 때문에 간단하게 처리가 가능합니다.
    else:
        return (x, y, 3 - move_dir)
    

# 구슬을 전부 한 번씩 움직여봅니다.
def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)


# 해당 구슬과 충돌이 일어나는 구슬이 있는지 확인합니다.
# 이를 위해 자신의 현재 위치에 놓은 구슬의 개수가
# 자신을 포함하여 2개 이상인지 확인합니다.
def duplicate_marble_exist(target_idx):
    target_x, target_y, _ = marbles[target_idx]
    
    return marble_cnt[target_x][target_y] >= 2
    

# 충돌이 일어나는 구슬을 전부 지워줍니다.
def remove_duplicate_marbles():
    global marbles
    
    # Step2-1 : 각 구슬의 위치에 count를 증가 시킵니다.
    for x, y, _ in marbles:
        marble_cnt[x][y] += 1

    # Step2-2 : 충돌이 일어나지 않은 구슬만 전부 기록합니다.
    remaining_marbles = [
        marble
        for i, marble in enumerate(marbles)
        if not duplicate_marble_exist(i)
    ]
    
    # Step2-3 : 나중을 위해 각 구슬의 위치에 적어놓은 count 수를 다시 초기화합니다.
    for x, y, _ in marbles:
        marble_cnt[x][y] -= 1
    
    # Step2-4 : 충돌이 일어나지 않은 구슬들로 다시 채워줍니다.
    marbles = remaining_marbles


# 조건에 맞춰 시뮬레이션을 진행합니다.
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 움직여봅니다.
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    remove_duplicate_marbles()


for _ in range(t):
    # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
    marbles = []
    
    # 입력
    n, m = tuple(map(int, input().split()))
    for _ in range(m):
        x, y, d = tuple(input().split())
        x, y = int(x), int(y)
        marbles.append((x, y, mapper[d]))
    
    # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
    # 시뮬레이션을 총 2 * n번 진행합니다.
    for _ in range(2 * n):
        simulate()
    
    # 출력
    print(len(marbles))
```
</div>
</details>

---

# 2. 백트래킹
## (1) K개 중 하나를 N번 선택하기
**재귀함수**
+ 어떤 함수 f가 해당 함수를 구현하는 데 동일한 함수 f를 다시 이용하는 경우
+ 종료 조건과 재귀 호출 부분으로 나뉨

<details>
<summary>순열 CODE</summary>
<div markdown="1">

```Python3
array = [1, 2, 3, 4, 5]
visited = [0] * 3

used = [0] * 5
def permutation(cnt):
    if cnt == 3:
        print(*visited)
        return
    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            visited[cnt] = array[i]
            permutation(cnt + 1)
            used[i] = 0
            visited[cnt] = 0

permutation(0)
```

</div>
</details>

<details>
<summary>중복 순열 CODE</summary>
<div markdown="1">

```Python3
array = [1, 2, 3, 4, 5]
visited = [0] * 3

def permutation_repetition(cnt):
    if cnt == 3:
        print(*visited)
        return
    for i in range(5):
        visited[cnt] = array[i]
        permutation_repetition(cnt + 1)
        visited[cnt] = 0

permutation_repetition(0)
```

</div>
</details>

<details>
<summary>조합 CODE</summary>
<div markdown="1">

```Python3
array = [1, 2, 3, 4, 5]
visited = [0] * 3

def combination(cnt, start):
    if cnt == 3:
        print(*visited)
        return
    for i in range(start, 5):
        visited[cnt] = array[i]
        combination(cnt + 1, i + 1)
        visited[cnt] = 0

combination(0, 0)
```
</div>
</details>

<details>
<summary>중복 조합 CODE</summary>
<div markdown="1">

```Python3
array = [1, 2, 3, 4, 5]
visited = [0] * 3

def combination_repetition(cnt, start):
    if cnt == 3:
        print(*visited)
        return
    for i in range(start, 5):
        visited[cnt] = array[i]
        combination_repetition(cnt + 1, i)
        visited[cnt] = 0

combination_repetition(0, 0)
```
</div>
</details>


**둘 중 하나를 N번 선택하기**
+ n이 3이었다면, 3자리를 만들어야 하며 각 자리마다 0 혹은 1이 채워져야 합니다. 따라서 먼저 첫 번째 자리에서 시작하여 0을 넣을지, 1을 넣을지 결정
+ 두 번째 자리에 0, 1 중 하나를 선택하여 적어줌
+ 세 번째 자리에도 0, 1 중 하나를 적어줌
+ 세 번째 자리까지 채워졌다면 현재 숫자(그림에서의 011)를 출력한 뒤, 그 다음 숫자를 만드는 것을 재귀적으로 반복
+ 각 과정에 걸쳐 숫자를 선택할 때마다 리스트에 각 숫자를 순서대로 넣어줍
+ C(4)에 오게 되었다면, 함수 정의상 네 번째 자리에 들어갈 숫자를 결정해야 하지만 N = 3이었기 때문에, 3번째 자리까지만 결정하면 되므로 더 진행하지 않고 현재 만들어진 리스트를 출력한 뒤, return를 통해 퇴각 $\rightarrow$ 즉 curr_num == n + 1인 경우가 종료조건
```Python3
# N자리의 2진수를 출력하는 코드
# Chooser(int curr_num) : curr_num번째 위치에 0 혹은 1을 선택하는 함수
n = 3
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = ' ')
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    answer.append(0)
    choose(curr_num + 1)
    answer.pop()

    answer.append(1)
    choose(curr_num + 1)
    answer.pop()
    
    return

choose(1)
```

---

**오답 문제 1 : 아름다운 수**
+ 문제 상황
    + 1이상 4이하의 숫자로만 이루어져 있으면서, 정확히 해당 숫자만큼 연달아 같은 숫자가 나오는 숫자를 아름다운 수라 함
    + n자리 아름다운 수가 몇 개 있는지를 구하는 프로그램을 작성
+ 알고리즘 설계
    + choose 함수를 통해 1이상 4이하의 숫자로 구성된 n자리 숫자를 모두 구현
    + 이후 beautiful num 함수를 통해 아름다운 수인지 각각 검사하고 개수를 구함
+ 틀린 이유
    + 처음부터 수를 구성하는 데에 있어 아름다운 수를 구현하려다보니 오류 발생
+ 수정
    + 구성할 수 있는 모든 n자리 수를 구현한 후 해당 수에 대해 아름다운 수인지 검사해 개수를 더함
+ 느낀 점
    + 시간 초과가 안 발생한다는 전제 하에 구현상 더 편리한 방법 사용하기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
n = int(input())
result = []

def beautiful_num(result):
    i = 0
    while True:
        num = result[i]
        if (i + num) > n:
            return False
            break
        if result[i : i + num] != [num] * num:
            return False
            break
        i = i + num
        if i == n:
            return True
            break
        if i > n:
            return False
            break

beautiful_cnt = 0
def choose(cnt):
    global beautiful_cnt
    if cnt == n:
        beautiful_cnt += int(beautiful_num(result))
        return
    for i in range(1, 5):
        result.append(i)
        choose(cnt + 1)
        result.pop()

choose(0)
print(beautiful_cnt)
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력:
n = int(input())
ans = 0
seq = list()


def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡습니다.
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아닙니다.
        if i + seq[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인합니다.
        # 하나라도 다른 숫자가 있다면
        # 아름다운 수가 아닙니다.
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
            
        i += seq[i]
        
    return True


def count_beautiful_seq(cnt):
    global ans
    
    if cnt == n:
        if is_beautiful():
            ans += 1
        return
	
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(0)
print(ans)
```
</div>
</details>

---

## (2) N개 중에 M개 고르기
+ n자리 이진 수 중 1의 개수가 정확히 m개인 수만 구해 출력하는 코드 $\rightarrow$ 지금까지의 1의 개수를 재귀함수의 인자로 정의하여 해결
+ 원하는 2진수 조합을 지금까지 만든 1의 개수를 관리하며 전부 만들어 보기 위해 Choose(int curr_num, int cnt) 이라는 함수를 이용
+ 종료조건은 curr_num이 n + 1인 경우로 걸어주고, 그 당시에 지금까지 선택한 1의 개수인 cnt가 m인 경우에만 해당 숫자를 출력해주면 됨
+ curr_num 자리에 0을 넣는 경우 : 리스트의 가장 끝에 숫자 0을 적어주고, 그 다음 자릿수인 curr_num + 1에 해당하는 함수 Choose(curr_num + 1, cnt)를 호출
+ curr_num 자리에 1을 넣는 경우 : 1의 개수가 1 증가하므로 Choose(curr_num + 1, cnt + 1)을 호출

```Python3
# Choose(int curr_num, int cnt): 지금까지 선택한 1의 개수가 cnt개라 했을 때, curr_num번째 위치에 0 혹은 1을 선택하는 함수
n, m = 3, 2
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = ' ')
    print()

def choose(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print_answer()
        return
    answer.append(0)
    choose(curr_num + 1, cnt)
    answer.pop()

    answer.append(1)
    choose(curr_num + 1, cnt + 1)
    answer.pop()
    
    return

choose(1, 0)
```

---

**오답 문제 1 : n개 중에 m개 뽑기**
+ 문제 상황
    + 1이상 N이하의 숫자 중 M개의 숫자를 골라 만들 수 있는 모든 조합을 구해주는 프로그램을 작성
+ 알고리즘 설계
    + 각각의 위치에 있는 숫자를 선택할 것인지 말 것인지에 대한 모든 가짓수에 대해 탐색하는 2^n 재귀를 생성
    + 그 중 정확히 m개가 선택된 경우만 출력하는 방식
    + 현재 어떤 숫자를 뽑을지 말지 고민중인지와 지금까지 선택한 숫자가 몇 개인지를 인자로 가지고 있어야 함
+ 틀린 이유
    + 백트래킹 이해 부족
+ 수정
    + X
+ 느낀 점
    + 조합 구현 코드 암기하기

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
combination = []


# 방문한 원소들을 출력해줍니다.
def print_combination():
    for elem in combination:
        print(elem, end = " ")
    
    print()


def find_combination(curr_num, cnt):
    # n개의 숫자를 모두 탐색했으면 더 이상 탐색하지 않습니다.
    if curr_num == n + 1:
        # 탐색하는 과정에서 m개의 숫자를 뽑은 경우 답을 출력해줍니다.
        if cnt == m:
            print_combination()
        return

    # curr_num에 해당하는 숫자를 사용했을 때의 경우를 탐색합니다.
    combination.append(curr_num)
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    # curr_num에 해당하는 숫자를 사용하지 않았을 때의 경우를 탐색합니다.
    find_combination(curr_num + 1, cnt)


find_combination(1, 0)
```
</div>
</details>

---

# 3. 그래프 탐색
## (1) DFS
**그래프**
+ 정점과 간선으로 이루어져 있는 자료구조. 정점간의 연결 관계가 간선을 이용하여 표현
+ 시작점으로부터 연결된 모든 정점을 전부 방문 + 이미 방문한 정점은 다시는 방문하지 않음음
+ 구현 방법
    + 인접 행렬
     	+ 두 정점 i, j가 연결관계에 있다면 graph[i][j]값을 1로, 그렇지 않다면 graph[i][j] 값을 0으로 정의하여 표현
        + 양방향 그래프라면 인접 행렬이 대칭인 모양, 단방향 그래프라면 X
        + 그래프에서 정점의 수를 V, 간선의 수를 E라 했을 때 인접 행렬 이용시 공간복잡도는 O($V^2$)
    + 인접 리스트
     	+ V개의 동적 배열을 만들어 관리
        + i번째 정점에 해당하는 동적 배열을 graph[i]
        + V개의 동적배열을 관리하는 리스트 1개와, 각 간선별로 정점이 2개씩 동적 배열에 각각 추가되므로 공간복잡도는 O(V + E)

**그래프에서의 DFS**
+ 깊이 우선 탐색 : 특정 정점에서 시작하여 갈 수 있는 곳까지 쭉 따라 들어갔다가 더 이상 갈 곳이 없으면 빠져나오는 방식의 그래프 탐색 방법
+ DFS는 꼭 재귀함수를 이용하여 작성
    + 시작점으로부터 연결된 모든 정점을 전부 방문
    + 이미 방문한 정점은 다시는 방문하지 않음
+ 구현 방법
    + 인접 행렬
     	+ graph라는 이름의 2차원 배열을 만들어, 두 정점이 연결되어 있다면 1 아니라면 0으로 표시
        + 첫 번째 인자인 vertex는 현재 위치를 의미
        + 현재 위치를 기준으로 연결된 정점을 탐색하기 위해서는 1번부터 정점의 개수인 VERTICES_NUM까지 for문 순회
        + 이 지점을 curr_v라 했을 때, graph[vertex][curr_v] 값이 1이면서 curr_v 정점에 방문했던 적이 없는지를 확인
        + visited : 방문했던 정점을 다시는 방문하지 않도록 하는 역할
        + 정점의 개수만큼의 크기를 갖는 visited 배열을 만들어 그 다음 DFS 함수를 호출하기 전에 꼭 해당 위치의 visited 값을 true로 변경하여, 다시는 탐색 도중에 해당 위치에 방문하지 않도록 해야함
		```Python3
		VERTICES_NUM = 7
		EDGES_NUM = 6
		
		graph = [
		    [0 for _ in range(VERTICES_NUM + 1)]
		    for _ in range(VERTICES_NUM + 1)
		]
		
		visited = [False for _ in range(VERTICES_NUM + 1)]
		
		def dfs(vertex):
		    for curr_v in range(1, VERTICES_NUM + 1):
			if graph[vertex][curr_v] and not visited[curr_v]:
			    print(curr_v)
			    visited[curr_v] = True
			    dfs(curr_v)
		start_points = [1, 1, 1, 2, 4, 6]
		end_points = [2, 3, 4, 5, 6, 7]
		
		for start, end in zip(start_points, end_points):
		    graph[start][end] = 1
		    graph[end][start] = 1
		
		root_vertex = 1
		print(root_vertex)
		visited[root_vertex] = True
		dfs(root_vertex)
		```
    + 인접 리스트
     	+ graph라는 이름의 1차원 배열을 만들고, graph[i]는 각각 i번째 정점에 연결되어 있는 정점들 목록을 관리하는 동적배열
        + 현재 위치를 vertex라 했을 때, 인접리스트에서는 연결된 정점이 전부 graph[vertex] 안에 리스트 형태로 들어있게 됨
        + graph[vertex] 에 들어있는 원소들을 순서대로 순회하면 해당 원소(curr_v)는 그 즉시 vertex에 연결되어 있는 원소가 됨
        + visited[curr_v]값이 false인지만 확인하여 방문되지 않은 정점에 대해서만 다음 탐색을 진행
        + 1번 정점에서 시작하여 연결되어 있으며 아직 방문해본 적이 없는 정점이 발견되면 visited 값을 true로 변경한 뒤, 다시 재귀적으로 해당 위치로 DFS 함수를 호출하는 것을 반복
		```Python3
		VERTICES_NUM = 7
		EDGES_NUM = 6
		
		graph = [[] for _ in range(VERTICES_NUM + 1)]
		visited = [False for _ in range(VERTICES_NUM + 1)]
		
		def dfs(vertex):
		    for curr_v in graph[vertex]:
		        if not visited[curr_v]:
		            print(curr_v)
		            visited[curr_v] = True
		            dfs(curr_v)
		
		start_points = [1, 1, 1, 2, 4, 6]
		end_points = [2, 3, 4, 5, 6, 7]
		
		for start, end in zip(start_points, end_points):
		    graph[start].append(end)
		    graph[end].append(start)
		
		root_vertex = 1
		print(root_vertex)
		visited[root_vertex] = True
		dfs(root_vertex)
		```
**격자에서의 DFS**
+ 현재 위치를 표현하기 위해서는 (x, y) 이렇게 2개의 값이 꼭 필요 : 행렬에서의 (i, j)와 같이 x행, y열을 의미
+ visited 배열 역시 2차원으로 구성
+ 구현 방법
    + 현재 위치 (x, y)로부터 갈 수 있는 곳들을 전부 탐색하여, 그 중 갈 수 있는 곳이 있다면, 해당 위치에 방문 체크를 해준 뒤 재귀함수를 다시 호출해주는 식으로 구현
    + dx, dy 테크닉을 이용하여 new_x, new_y에 인접한 칸의 위치가 오도록 설정
    + 인접한 위치 (new_x, new_y)로 이동해야 할 필요가 있다면, visited 값을 1로 설정해주고 재귀함수를 호출
    + visited 배열에 방문 표시를 하는 위치를 꼭 재귀 함수 호출 전에 하지 않고, 재귀 함수에 진입하는 순간에 진행하는 것 역시 가능
    + 다만 BFS 탐색에서는 꼭 queue에 넣기 전에 visited 배열에 방문 표시를 해야 하므로, 가능하면 DFS 탐색 시에도 재귀 함수 호출 직전에 visited 표기를 하는 패턴으로 연습
	```Python3
	answer = [[0 for _ in range(5)] for _ in range(5)]
	visited = [[0 for _ in range(5)] for _ in range(5)]
	order = 1
	
	def in_range(x, y):
	    return 0 <= x and x < 5 and 0 <= y and y < 5
	
	def can_go(x, y):
	    if not in_range(x, y):
	        return False
	    
	    if visited[x][y] or grid[x][y] == 0:
	        return False
	    
	    return True
	
	def dfs(x, y):
	    global order
	    dxs, dys = [1, 0], [0, 1]
	    for dx, dy in zip(dxs, dys):
	        new_x, new_y = x + dx, y + dy
	        if can_go(new_x, new_y):
	            answer[new_x][new_y] = order
	            order += 1
	            visited[new_x][new_y] = 1
	            dfs(new_x, new_y)
	
	answer[0][0] = order
	order += 1
	visited[0][0] = 1
	dfs(0, 0)
	```

---

## (2) BFS 탐색
**BFS**
+ 너비 우선 탐색 : 시작점을 기준으로 가장 가까운 곳부터 순서대로 탐색을 진행하는 방식
+ BFS는 꼭 재귀함수 없이 queue라는 자료구조를 이용하여 작성
    + BFS - queue를 이용해 지금까지 방문한 노드들을 관리
    + DFS - 새로 방문하게 되는 위치가 생기면 해당 위치를 DFS함수의 인자로 넘기며 재귀함수를 호출해 탐색을 재개
+ DFS는 재귀함수로 새로 찾은 노드를 넘기지만, BFS는 새로 찾은 노드를 큐에 추가하고 탐색을 유지하기 위해 queue가 empty가 되기 전까지 계속 진행한다는 점에서의 차이
+ 구현 방법
    + 인접 행렬
    	+ graph라는 이름의 2차원 배열을 만들어, 두 정점이 연결되어 있다면 1 아니라면 0으로 표시
     	+ 새로 방문하게 되는 노드를 queue에 계속 넣어주며, queue가 empty 상태가 되기 전까지 queue에서 가장 앞에 있는 원소를 pop하여 해당 원소를 현재 원소의 위치로 설정
        + BFS에서는 queue에서 뽑힌 위치 curr_v가 현재 위치가 됨
        + 현재 위치를 기준으로 연결된 정점을 탐색하기 위해서는 1번부터 정점의 개수인 VERTICES_NUM까지 for문 순회
        + 이 지점을 next_v라 했을 때, graph[curr_v][next_v] 값이 1이면서 next_v 정점에 방문했던 적이 없는 지를 확인
        + 정점의 개수만큼의 크기를 갖는 visited 배열을 만들어 queue에 새로운 위치를 넣어주는 순간에 꼭 해당 위치의 visited 값을 true로 변경하여, 다시는 탐색 도중에 해당 위치에 방문하지 않도록 해야만 함
        + 1번 정점에서 시작하여 연결되어 있으며 아직 방문해본 적이 없는 정점이 발견되면 visited 값을 true로 변경한 뒤 계속 탐색을 진행하게 됨
		```Python3
		from collections import deque
		
		VERTICES_NUM = 7
		EDGES_NUM = 6
		
		graph = [
		    [0 for _ in range(VERTICES_NUM + 1)]
		    for _ in range(VERTICES_NUM + 1)
		]
		visited = [False for _ in range(VERTICES_NUM + 1)]
		q = deque()
		
		def bfs():
		    while q:
		        curr_x = q.popleft()
		        for next_v in range(1, VERTICES_NUM +1):
		            if graph[curr_x][next_v] and not visited[next_v]:
		                print(next_v)
		                visited[next_v] = True
		                q.append(next_v)
		
		start_points = [1, 1, 1, 2, 4, 6]
		end_points = [2, 3, 4, 5, 6, 7]
		
		for start, end in zip(start_points, end_points):
		    graph[start][end] = 1
		    graph[end][start] = 1
		
		root_vertex = 1
		print(root_vertex)
		visited[root_vertex] = True
		q.append(root_vertex)
		bfs()
		```
    + 인접 리스트
     	+ graph라는 이름의 1차원 배열을 만들고, graph[i]는 각각 i번째 정점에 연결되어 있는 정점들 목록을 관리하는 동적배열
        + 인접 행렬을 이용하는 경우와 마찬가지로 queue를 이용, 연결된 정점을 찾아내는 방법만 조금 다름
        + 현재 위치를 vertex라 했을 때, 인접리스트에서는 연결된 정점이 전부 graph[vertex] 안에 리스트 형태로 들어있게 됨
        + graph[vertex]에 들어있는 원소들을 순서대로 순회하면 해당 원소(curr_v)는 그 즉시 vertex에 연결되어 있는 원소가 됨
        + visited[curr_v]값이 false인지만 확인하여 방문되지 않은 정점에 대해서만 다음 탐색을 진행
        + 1번 정점에서 시작하여 연결되어 있으며 아직 방문해본 적이 없는 정점이 발견되면 visited 값을 true로 변경한 뒤 계속 탐색을 진행
		```Python3
		from collections import deque
		
		VERTICES_NUM = 7
		EDGES_NUM = 6
		
		graph = [[] for _ in range(VERTICES_NUM + 1)]
		visited = [False for _ in range(VERTICES_NUM + 1)]
		q = deque()
		
		def bfs():
		    while q:
		        curr_x = q.popleft()
		        for next_v in graph[curr_x]:
		            if not visited[next_v]:
		                print(next_v)
		                visited[next_v] = True
		                q.append(next_v)
		
		start_points = [1, 1, 1, 2, 4, 6]
		end_points = [2, 3, 4, 5, 6, 7]
		
		for start, end in zip(start_points, end_points):
		    graph[start].append(end)
		    graph[end].append(start)
		
		root_vertex = 1
		print(root_vertex)
		visited[root_vertex] = True
		q.append(root_vertex)
		bfs()
		```

**격자에서의 BFS**
+ 격자 문제에서는 굳이 그래프를 표현하기 위한 인접 행렬 혹은 인접 리스트를 만들어줄 필요가 없음
+ queue가 필요하며, queue에 각 노드의 위치를 넣어야 함
+ 격자에서의 BFS 탐색에서 현재 위치를 표현하기 위해서는 (x, y) 이렇게 2개의 값이 꼭 필요. 여기서 (x, y)는 수학에서의 x, y가 아닌 행렬에서의 (i, j)와 같이 x행, y열을 의미
+ BFS는 queue가 empty 상태가 되기 전까지 계속 탐색을 반복
+ DFS는 함수의 인자 값으로 현재 위치를 반환해주지만, BFS는 현재 queue에서 가장 앞에 있는 원소를 현재 위치로 설정
+ 꼭 queue에서 해당 원소를 pop 해줘야만 함에 유의
+ 구현 방법
	+ 현재 위치 (x, y)가 정해졌다면, 이 위치로부터 갈 수 있는 곳들을 전부 탐색하여 그 중 갈 수 있는 곳이 있다면, 해당 위치에 방문 체크를 해준 뒤 해당 위치를 queue에 넣어주는 식으로 구현
	+ dx, dy 테크닉을 이용하여 new_x, new_y에 인접한 칸의 위치가 오도록 설정
	+ 인접한 위치 (new_x, new_y)로 이동해야 할 필요가 있다면, visited 값을 true로 설정해주고 queue에 해당 위치를 넣어줌
	+ (new_x, new_y)로 이동해도 되는지를 판단해주는 함수를 편의상 CanGo라고 작성
	+ 이 조건을 만족하는 경우에만 새로 queue에 넣어주기
	```Python3
	def in_range(x, y):
	    return 0 <= x and x < 5 and 0 <= y and y < 5
	
	def can_go(x, y):
	    if not in_range(x, y):
	        return False
	    if visited[x][y] or grid[x][y] == 0:
	        return False
	    return True
	
	def push(x, y):
	    global order
	    answer[x][y] = order
	    order += 1
	    visited[x][y] = True
	    q.append((x, y))
	
	def bfs():
	    dxs = [1, 0]
	    dys = [0, 1]
	
	    while q:
	        x, y = q.popleft()
	        for dx, dy in zip(dxs, dys):
	            new_x, new_y = x + dx, y + dy
	            if can_go(new_x, new_y):
	                push(new_x, new_y)
	
	push(0, 0)
	bfs()
	```

---

**오답 문제 1 : 갈 수 있는 곳들**
+ 문제 상황
    + 숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 구하는 프로그램을 작성
    + 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 해당 칸이 이동할 수 없는 곳임을 의미
    + ```1 ≤ r ≤ n, 1 ≤ c ≤ n```
+ 알고리즘 설계
    + queue에 주어진 출발점들을 담고 bfs 내에서 꺼내서 쓰도록 설계
+ 틀린 이유
    + 각각의 출발점에 대해서 bfs를 for문으로 돌려 한 곳에 모아서 결과값을 내려다보니 시간 초과 발생
+ 수정
    + 어차피 popleft 통해서 다 순회하게 되기 때문에 주어진 출발점들을 모두 queue에 넣고 bfs 한 번에 돌려버리기
+ 느낀 점
    + 문제 상황에 맞는 bfs 적용 익히기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
from collections import deque

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    q.append((r - 1, c - 1))
    visited[r - 1][c - 1] = 1

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def bfs(graph, visited):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

bfs(graph, visited)

cnt = 0
for row in visited:
    cnt += sum(row)
print(cnt)
```
</div>
</details>

---

**오답 문제 2 : 돌 잘 치우기**
+ 문제 상황
    + 숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, 주어진 돌 중 m개의 돌만 적절하게 치워 k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 최대로 하는 프로그램을 작성
    + 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 돌이 있어 해당 칸이 이동할 수 없는 곳임을 의미
    + ```3 ≤ n ≤ 100 / 1 ≤ k ≤ n * n / 0 ≤ m ≤ 입력으로 주어지는 초기 돌의 개수 ≤ 8```
+ 알고리즘 설계
    + backtracking을 통해 격자 내에 주어진 돌 중에 적절히 m개를 선택
    + 각 선택마다 k개의 시작점들을 queue에 집어넣어 bfs 탐색 진행
+ 틀린 이유
    + backtracking n개 중에 m개 고르기 과정에서 오류가 발생했음
+ 수정
    + 조합 구현 코드 수정
+ 느낀 점
    + 조합을 backtracking으로 구현하는 방법 암기

<details>
<summary>풀이 CODE</summary>
<div markdown="1">

```Python3
from collections import deque

n, k, m = map(int, input().split())
graph = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

rock = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            rock.append((i, j))

q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    visited[r - 1][c - 1] = 1
    q.append((r - 1, c - 1))

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def bfs(graph, q, visited):
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

num_rock = len(rock)
combination_result = []
combination_visited = [0] * m

bfs_sum_list = []
def combination(cnt, start):
    global combination_result, bfs_sum_list

    bfs_graph = [g[:] for g in graph]
    bfs_q = q.copy()
    bfs_visited = [v[:] for v in visited]
    bfs_result = []
    if cnt == m:
        for j in combination_visited:
            bfs_graph[j[0]][j[1]] = 0

        bfs(bfs_graph, bfs_q, bfs_visited)
        bfs_sum = 0
        max_bfs_sum = 0
        for row in bfs_visited:
            bfs_sum += sum(row)
        max_bfs_sum = max(max_bfs_sum, bfs_sum)
        bfs_sum_list.append(max_bfs_sum)
        return
    for i in range(start, num_rock):
        combination_visited[cnt] = rock[i]
        combination(cnt + 1, i + 1)
        combination_visited[cnt] = 0

combination(0, 0)
print(max(bfs_sum_list))
```
</div>
</details>

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3
from collections import deque

# 변수 선언 및 입력
n, k, m = tuple(map(int, input().split()))
a = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
s_pos = []
stone_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if a[i][j] == 1
]
selected_stones = []

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_range(x, y) and not a[x][y] and not visited[x][y]


def bfs():
    # queue에 남은 것이 없을때까지 반복합니다.
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()

        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부를 표시해줍니다. 
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


def calc():
    for x, y in selected_stones:
        a[x][y] = 0
	
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
		
    # k개의 시작점을 queue에 넣고 시작합니다.
	# BFS는 여러 시작점에서 시작하여
    # 이동 가능한 칸을 전부 탐색하는 것이 가능합니다.
    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True

    bfs()
	
    for x, y in selected_stones:
        a[x][y] = 1
        
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    
    return cnt


def find_max(idx, cnt):
    global ans
    
    if idx == len(stone_pos):
        if cnt == m:
            ans = max(ans, calc())
        return

    selected_stones.append(stone_pos[idx])
    find_max(idx + 1, cnt + 1)
    selected_stones.pop()
	
    find_max(idx + 1, cnt)


for _ in range(k):
    r, c = tuple(map(int, input().split()))
    s_pos.append((r - 1, c - 1))
    
find_max(0, 0)
print(ans)
```
</div>
</details>

---



## (3) 가중치가 동일한 그래프에서의 BFS

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

<details>
<summary>해설 CODE</summary>
<div markdown="1">

```Python3

```
</div>
</details>

---
