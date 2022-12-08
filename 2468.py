# https://www.acmicpc.net/problem/2468
from collections import deque
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
for b in board:
    max_val = max(max_val, max(b))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def set_board(limit):
    for i in range(n):
        for j in range(n):
            if board[i][j] <= limit:
                board[i][j] = -1

def dfs(x, y, visited, limit):
    stack = deque([(x, y)])
    while stack:
        nx, ny = stack.pop()
        for i in range(4):
            mx, my = nx + dx[i], ny + dy[i]
            if 0 <= mx < n and 0 <= my < n and board[mx][my] > limit and visited[mx][my] == 0:
                visited[mx][my] = 1
                stack.append((mx, my))

ans = 0

for i in range(max_val + 1):
    tmp = 0
    visited = [[0] * n for _ in range(n)]
    set_board(i)
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and board[j][k] > i:
                visited[j][k] = 1
                dfs(j, k, visited, i)
                tmp += 1
    ans = max(ans, tmp)
print(ans)
