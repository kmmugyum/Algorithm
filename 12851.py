# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
dx = [1, -1]

current, target = map(int, input().split())

que = deque([(current, 0)])
visited = [current]


def bfs_check_min_time(cur):
    # 최소의 시간을 탐색

    que = deque([(cur, 0)])
    while que:
        nx, cnt = que.popleft()
        if nx == target:
            return cnt
        for i in range(3):
            if i <= 1:
                mx = nx + dx[i]
            else:
                mx = nx * 2
            if mx not in visited:
                visited.append(mx)
                que.append((mx, cnt + 1))


def dfs_to_sol_cnt(cur, cnt, visited, lim):
    global ans
    if cnt == lim and visited[-1] == target:
        ans += 1
        return
    if cnt > lim:
        return

    for i in range(3):
        if i <= 1:
            mx = cur + dx[i]
        else:
            mx = cur * 2

        if mx not in visited:
            visited.append(mx)
            dfs_to_sol_cnt(mx, cnt + 1, visited, lim)
            visited.pop()


min_time = bfs_check_min_time(current)
print(min_time)
visited = [current]
ans = 0
dfs_to_sol_cnt(current, 0, visited, min_time)
print(ans)