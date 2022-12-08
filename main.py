from collections import deque
board = []
dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
def bfs(x, y, visited):
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft()
        for i in range(len(dx)):
            mx, my = nx + dx[i], ny + dy[i]
            if 0 <= mx < b and 0 <= my < a and visited[mx][my] == 0 and board[mx][my] == 1:
                visited[mx][my] = 1
                queue.append((mx, my))


while True:
    a, b = map(int, input().split())
    visited =[[0] * a for _ in range(b)]
    cnt = 0
    if a == 0 and b == 0:
        break
    board = [(list(map(int, input().split()))) for _ in range(b)]
    for i in range(b):
        for j in range(a):
            if visited[i][j] == 0 and board[i][j] == 1:
                visited[i][j] = 1
                bfs(i, j, visited)
                cnt += 1
    print(cnt)